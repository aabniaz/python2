import numpy as np
import matplotlib.pyplot as plt

# параметры сетки и физические параметры
dx = 0.01
dy = 0.01
dt = 0.0001
Re = 100
dens = 1000
visc = 1/Re

# критерии остановки
eps = 1e-6
eps_P = 1e-6
max_it = 1e4
max_it_P = 1e6

# скорости ввода
speed_U = 1
speed_P = 1

# размер сетки
x = np.arange(0, 1 + dx, dx)
y = np.arange(0, 1 + dy, dy)
N = len(x)
S = len(y)

# определение областей
S1 = int(0.2/dy)
S2 = int(0.8/dy)
S3 = int(0.4/dx)

# инициализация полей U, V, P
u_init = np.zeros((S, N))
u_pred = np.zeros((S, N))
u_corr = np.zeros((S, N))
v_init = np.zeros((S, N))
v_pred = np.zeros((S, N))
v_corr = np.zeros((S, N))
P_init = np.zeros((S, N))
P_corr = np.zeros((S, N))

# начальные и граничные условия
# в начальный момент времени
u_init[:, :] = 0
v_init[:, :] = 0
P_init[:, :] = 0

# в области ввода inlet
u_init[S2:, 0:S3] = 1
v_init[S2:, 0:S3] = 0
P_init[S2:, 0:S3] = 1

# на стенах walls
u_init[0:S2, 0:S3] = 0
u_init[0, S3:] = 0
u_init[S-1, :] = 0

v_init[0:S2, 0:S3] = 0
v_init[0, S3:] = 0
v_init[S-1, :] = 0

P_init[0:S2, 0:S3-1] = P_init[0:S2, 1:S3]
P_init[0, S3:] = P_init[1, S3:]
P_init[S-1, :] = P_init[S-2, :]

# на выходе outlet
u_init[:, N-1] = u_init[:, N-2]
v_init[:, N-1] = 0
P_init[:, N-1] = 0

# инициализация переменных для итераций
max = 1
iter = 0

# основной цикл по времени
while max > eps and iter < max_it:
    
    # шаг 1: уравнение Burgers
    u_pred[1:-1, 1:-1] = u_init[1:-1, 1:-1] - dt*(u_init[1:-1, 1:-1]*(u_init[1:-1, 2:] - u_init[1:-1, 0:-2])/(2*dx) \
        + v_init[1:-1, 1:-1]*(u_init[2:, 1:-1] - u_init[0:-2, 1:-1])/(2*dy) \
        - visc*((u_init[1:-1, 2:] - 2*u_init[1:-1, 1:-1] + u_init[1:-1, 0:-2])/dx**2 + (u_init[2:, 1:-1] - 2*u_init[1:-1, 1:-1] \
            + u_init[0:-2, 1:-1])/dy**2))
    
    v_pred[1:-1, 1:-1] = v_init[1:-1, 1:-1] - dt*(
        u_init[1:-1, 1:-1]*(v_init[1:-1, 2:] - v_init[1:-1, 0:-2])/(2*dx) + v_init[1:-1, 1:-1]*(v_init[2:, 1:-1] - v_init[0:-2, 1:-1])/(2*dy) \
        - visc*((v_init[1:-1, 2:] - 2*v_init[1:-1, 1:-1] + v_init[1:-1, 0:-2])/dx**2 \
            + (v_init[2:, 1:-1] - 2*v_init[1:-1, 1:-1] + v_init[0:-2, 1:-1])/dy**2))
    
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
    
    # шаг 2: уравнение Poisson
    while max_P > eps_P and iter_P < max_it_P:

        P_corr[1:-1, 1:-1] = (dy**2*(P_init[1:-1, 2:] + P_init[1:-1, 0:-2]) + dx**2*(P_init[2:, 1:-1] + P_init[0:-2, 1:-1]))/(2*(dx**2 + dy**2)) \
                - dx**2*dy**2*dens/(2*dt*(dx**2 + dy**2)) * ((u_pred[1:-1, 2:] - u_pred[1:-1, 0:-2])/(2*dx) \
                + (v_pred[2:, 1:-1] - v_pred[0:-2, 1:-1])/(2*dy))

        P_corr[0:S2, 0:S3-1] = P_corr[0:S2, 1:S3]
        P_corr[S2:, 0:S3] = 1
        P_corr[:, N-1] = 0
        P_corr[0, S3:] = P_corr[1, S3:]
        P_corr[S-1, :] = P_corr[S-2, :]
        maximum_P = np.max(np.abs(P_corr - P_init))
        P_init[:, :] = P_corr[:, :]
        iter_P += 1
    
    # шаг 3: корректор
    u_corr[1:-1, 1:-1] = u_pred[1:-1, 1:-1] - dt/dens * (P_corr[1:-1, 2:] - P_corr[1:-1, 0:-2])/(2*dx)  
    v_corr[1:-1, 1:-1] = v_pred[1:-1, 1:-1] - dt/dens * (P_corr[2:, 1:-1] - P_corr[0:-2, 1:-1])/(2*dy)

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
        
    maximum = np.max(np.abs(u_corr - u_init))
    u_init[:, :] = u_corr[:, :]
    v_init[:, :] = v_corr[:, :]
    
    iter += 1

# создание сетки для визуализации
X, Y = np.meshgrid(x, y)

# визуализация U, V, P
# U
plt.contourf(X, Y, u_corr)
plt.colorbar(label='u')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('U')

# V
plt.contourf(X, Y, v_corr)
plt.colorbar(label='v')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('V')

# P
plt.contourf(X, Y, P_corr)
plt.colorbar(label='p')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('P')
plt.contour(X, Y, P_corr)
plt.streamplot(X, Y, u_corr, v_corr)
plt.show()