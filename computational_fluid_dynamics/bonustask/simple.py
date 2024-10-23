import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры сетки и времени
dx = 0.027
dy = 0.027
dt = 0.00001
Re = 1
dens = 1
visc = 1/Re
alpha = 0.7

# Константы для остановки итераций
e = 1e-6
stop_it = 1e4
stop_it_P = 1e6

# Создание сетки
x = np.arange(0, dx+1, dx)
y = np.arange(0, dy+1, dy)
N = len(x)
S = len(y)

# Задание начальных условий
S1 = int(0.2/dy)
S2 = int(0.8/dy)
S3 = int(0.4/dx)

# Задание начальных условий
u_init = np.zeros((S, N))
u_pred = np.zeros((S, N))
u_corr = np.zeros((S, N))

v_init = np.zeros((S, N))
v_pred = np.zeros((S, N))
v_corr = np.zeros((S, N))

p_init = np.zeros((S, N))
p_pred = np.random.rand(S, N)
p_corr = np.zeros((S, N))

# at t=0:
u_init[:, :] = 0
v_init[:, :] = 0
p_init[:, :] = 0

# inlet 
u_init[S2:, 0:S3] = 1
v_init[S2:, 0:S3] = 0
p_init[S2:, 0:S3] = 1

# walls 
u_init[0:S2, 0:S3] = 0
u_init[0, S3:] = 0
u_init[S-1, :] = 0

v_init[0:S2, 0:S3] = 0
v_init[0, S3:] = 0
v_init[S-1, :] = 0

p_init[0:S2, 0:S3-1] = p_init[0:S2, 1:S3]
p_init[0, S3:] = p_init[1, S3:]
p_init[S-1, :] = p_init[S-2, :]

# outlet
u_init[:, N-1] = u_init[:, N-2]
v_init[:, N-1] = 0
p_init[:, N-1] = 0

p_pred[:, :] = 0

max = 1
iter = 0
while max > e and iter < stop_it:
    # Шаг 1: Предсказание компонент скорости 
    u_pred[1:-1, 1:-1] = u_init[1:-1, 1:-1] - dt*(
        u_init[1:-1, 1:-1]*(u_init[1:-1, 2:] - u_init[1:-1, 0:-2])/(2*dx) \
        + v_init[1:-1, 1:-1]*(u_init[2:, 1:-1] - u_init[0:-2, 1:-1])/(2*dy) \
        - visc*(
            (u_init[1:-1, 2:] - 2*u_init[1:-1, 1:-1] + u_init[1:-1, 0:-2])/dx**2 \
            + (u_init[2:, 1:-1] - 2*u_init[1:-1, 1:-1] + u_init[0:-2, 1:-1])/dy**2) +
                1/dens*(p_pred[2:, 1:-1] - p_pred[0:-2, 1:-1])/2*dx)
    
    v_pred[1:-1, 1:-1] = v_init[1:-1, 1:-1] - dt*(
        u_init[1:-1, 1:-1]*(v_init[1:-1, 2:] - v_init[1:-1, 0:-2])/(2*dx) \
        + v_init[1:-1, 1:-1]*(v_init[2:, 1:-1] - v_init[0:-2, 1:-1])/(2*dy) \
        - visc*(
            (v_init[1:-1, 2:] - 2*v_init[1:-1, 1:-1] + v_init[1:-1, 0:-2])/dx**2 \
            + (v_init[2:, 1:-1] - 2*v_init[1:-1, 1:-1] + v_init[0:-2, 1:-1])/dy**2) +
                1/dens*(p_pred[1:-1, 2:] - p_pred[1:-1, 0:-2])/2*dy)
    
    u_pred[0, S3:] = 0
    u_pred[S-1, :] = 0
    u_pred[0:S2, 0:S3] = 0
    u_pred[S2:, 0:S3] = 1
    u_pred[:, N-1] = u_pred[:, N-2]
    
    v_pred[0, S3:] = 0
    v_pred[S-1, :] = 0
    v_pred[:, 0:S3] = 0
    v_pred[:, N-1] = 0

    max_P = 1
    iter_P = 0
    
    # Шаг 2: Решение уравнения для давления
    while max_P > e and iter_P < stop_it_P:

        p_corr[1:-1, 1:-1] = (dy**2*(p_init[1:-1, 2:] + p_init[1:-1, 0:-2]) \
            + dx**2*(p_init[2:, 1:-1] + p_init[0:-2, 1:-1]))/(2*(dx**2 + dy**2)) \
                - dx**2*dy**2*dens/(2*dt*(dx**2 + dy**2)) \
                * ((u_pred[1:-1, 2:] - u_pred[1:-1, 0:-2])/(2*dx) \
                + (v_pred[2:, 1:-1] - v_pred[0:-2, 1:-1])/(2*dy))

        p_corr[0:S2, 0:S3-1] = p_corr[0:S2, 1:S3]
        p_corr[S2:, 0:S3] = 1
        p_corr[:, N-1] = 0
        p_corr[0, S3:] = p_corr[1, S3:]
        p_corr[S-1, :] = p_corr[S-2, :]
        
        max_P = np.max(np.abs(p_corr - p_init))        
        p_init[:, :] = p_corr[:, :]
        iter_P += 1
        
        
    # Шаг 3: Коррекция компонент скорости
    u_corr[1:-1, 1:-1] = u_pred[1:-1, 1:-1] - dt/dens * (p_corr[1:-1, 2:] - p_corr[1:-1, 0:-2])/(2*dx)  
    v_corr[1:-1, 1:-1] = v_pred[1:-1, 1:-1] - dt/dens * (p_corr[2:, 1:-1] - p_corr[0:-2, 1:-1])/(2*dy)
        
    u_corr[0:S2, 0:S3] = 0
    u_corr[S2:, 0:S3] = 1
    u_corr[:, N-1] = u_corr[:, N-2]
    u_corr[0, :] = 0
    u_corr[S-1, :] = 0
    v_corr[0:S2, 0:S3] = 0
    v_corr[S2:, 0:S3] = 0
    v_corr[:, N-1] = v_corr[:, N-2]
    v_corr[0, :] = 0
    v_corr[S-1, :] = 0
        
    # Шаг 4: Коррекция давления
    p_pred[1:-1, 1:-1] = p_corr[1:-1, 1:-1] - alpha * ((p_corr[1:-1, 2:] - p_corr[1:-1, 0:-2])/(2*dx) + (p_corr[2:, 1:-1] - p_corr[0:-2, 1:-1])/(2*dy))

    max = np.max(np.abs(u_corr - u_init))
    u_init[:, :] = u_corr[:, :]
    v_init[:, :] = v_corr[:, :]
    print(max)
    
    iter += 1
    
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.contourf(X, Y, u_corr, cmap='viridis', levels=20)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('u')

plt.subplot(132)
plt.contourf(X, Y, v_corr, cmap='viridis', levels=20)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('v')

plt.subplot(133)
plt.contourf(X, Y, p_corr, cmap='viridis', levels=20)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('p')
plt.contour(X, Y, p_corr)
plt.streamplot(X, Y, u_corr, v_corr)

plt.tight_layout()
plt.show()
