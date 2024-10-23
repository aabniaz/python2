import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dx = 0.01
dy = 0.01
dt = 0.0001
Re = 100
rho = 1000
nu = 1/Re

eps = 1e-6
eps_P = 1e-6
speed_U = 1
speed_P = 1
stop_iteration = 1e4
stop_iteration_P = 1e6

x = np.arange(0, 1 + dx, dx)
y = np.arange(0, 1 + dy, dy)
N = len(x)
M = len(y)

M1 = int(0.2/dy)
M2 = int(0.8/dy)
M3 = int(0.4/dx)

U_old = np.zeros((M, N))
U_s = np.zeros((M, N))
U_new = np.zeros((M, N))

V_old = np.zeros((M, N))
V_s = np.zeros((M, N))
V_new = np.zeros((M, N))

P_old = np.zeros((M, N))
P_new = np.zeros((M, N))

# at t=0:
U_old[:, :] = 0
V_old[:, :] = 0
P_old[:, :] = 0

# inlet (где жидкость вводится, типа коридорчика)
# U(t, 0<x<0.4, 0.8<y<L) = 1
# V(t, 0<x<0.4, 0.8<y<L) = 0
# P(t, 0<x<0.4, 0.8<y<L) = 1
U_old[M2:, 0:M3] = 1
V_old[M2:, 0:M3] = 0
P_old[M2:, 0:M3] = 1

# walls (3 горизонтальных?? (2 верm, и одна в инлете), 2 вертикальных)
# U(t, 0<x<0.4, 0<y<0.8) = 0
# U(t, 0.4<x<L, y=0) = 0
# U(t, x, y=L) = 0
U_old[0:M2, 0:M3] = 0
U_old[0, M3:] = 0
U_old[M-1, :] = 0

# V(t, 0<x<0.4, 0<y<0.8) = 0
# V(t, 0.4<x<1, y=0) = 0
# V(t, x, y=1) = 0
V_old[0:M2, 0:M3] = 0
V_old[0, M3:] = 0
V_old[M-1, :] = 0

# Px(t, 0<x<0.4, 0<y<0.8) = 0  ==> 
# Py(t, 0.4<x<1, y=0) = 0
# Py(t, x, y=1) = 0
P_old[0:M2, 0:M3-1] = P_old[0:M2, 1:M3]
P_old[0, M3:] = P_old[1, M3:]
P_old[M-1, :] = P_old[M-2, :]

# outlet (полностью открытая стена)
# Ux(t, x=L, 0<y<1) = 0
# V(t, x=L, 0<y<1) = 0
# P(t, x=L, 0<y<1) = 0
U_old[:, N-1] = U_old[:, N-2]
V_old[:, N-1] = 0
P_old[:, N-1] = 0


max = 1
iter = 0
while max > eps and iter < stop_iteration:
    
    #step 1: Burgers eq
    U_s[1:-1, 1:-1] = U_old[1:-1, 1:-1] - dt*(
        U_old[1:-1, 1:-1]*(U_old[1:-1, 2:] - U_old[1:-1, 0:-2])/(2*dx) \
        + V_old[1:-1, 1:-1]*(U_old[2:, 1:-1] - U_old[0:-2, 1:-1])/(2*dy) \
        - nu*(
            (U_old[1:-1, 2:] - 2*U_old[1:-1, 1:-1] + U_old[1:-1, 0:-2])/dx**2 \
            + (U_old[2:, 1:-1] - 2*U_old[1:-1, 1:-1] + U_old[0:-2, 1:-1])/dy**2
            )
        )
    
    V_s[1:-1, 1:-1] = V_old[1:-1, 1:-1] - dt*(
        U_old[1:-1, 1:-1]*(V_old[1:-1, 2:] - V_old[1:-1, 0:-2])/(2*dx) \
        + V_old[1:-1, 1:-1]*(V_old[2:, 1:-1] - V_old[0:-2, 1:-1])/(2*dy) \
        - nu*(
            (V_old[1:-1, 2:] - 2*V_old[1:-1, 1:-1] + V_old[1:-1, 0:-2])/dx**2 \
            + (V_old[2:, 1:-1] - 2*V_old[1:-1, 1:-1] + V_old[0:-2, 1:-1])/dy**2
            )
        )
    
    U_s[0, M3:] = 0
    U_s[M-1, :] = 0
    U_s[0:M2, 0:M3] = 0
    U_s[M2:, 0:M3] = 1
    U_s[:, N-1] = U_s[:, N-2]
    
    V_s[0, M3:] = 0
    V_s[M-1, :] = 0
    V_s[:, 0:M3] = 0
    V_s[:, N-1] = 0
    
    max_P = 1
    iter_P = 0
    
    # step 2: Poissons eq
    while max_P > eps_P and iter_P < stop_iteration_P:

        P_new[1:-1, 1:-1] = (dy**2*(P_old[1:-1, 2:] + P_old[1:-1, 0:-2]) \
            + dx**2*(P_old[2:, 1:-1] + P_old[0:-2, 1:-1]))/(2*(dx**2 + dy**2)) \
                - dx**2*dy**2*rho/(2*dt*(dx**2 + dy**2)) \
                * ((U_s[1:-1, 2:] - U_s[1:-1, 0:-2])/(2*dx) \
                + (V_s[2:, 1:-1] - V_s[0:-2, 1:-1])/(2*dy))

        P_new[0:M2, 0:M3-1] = P_new[0:M2, 1:M3]
        P_new[M2:, 0:M3] = 1
        P_new[:, N-1] = 0
        P_new[0, M3:] = P_new[1, M3:]
        P_new[M-1, :] = P_new[M-2, :]
        
        maximum_P = np.max(np.abs(P_new - P_old))
        # print(maximum_P, iteration_P)
        
        P_old[:, :] = P_new[:, :]
        
        iter_P += 1
    
    # step 3: Corrector
    U_new[1:-1, 1:-1] = U_s[1:-1, 1:-1] - dt/rho * (P_new[1:-1, 2:] - P_new[1:-1, 0:-2])/(2*dx)  
    V_new[1:-1, 1:-1] = V_s[1:-1, 1:-1] - dt/rho * (P_new[2:, 1:-1] - P_new[0:-2, 1:-1])/(2*dy)

    U_new[0:M2, 0:M3] = 0
    U_new[M2:, 0:M3] = 1
    U_new[:, N-1] = U_new[:, N-2]
    U_new[0, :] = 0
    U_new[M-1, :] = 0

    V_new[0:M2, 0:M3] = 0
    V_new[M2:, 0:M3] = 0
    V_new[:, N-1] = V_new[:, N-2]
    V_new[0, :] = 0
    V_new[M-1, :] = 0
        
    maximum = np.max(np.abs(U_new - U_old))
    U_old[:, :] = U_new[:, :]
    V_old[:, :] = V_new[:, :]
#     print(maximum)
    
    iter += 1

X, Y = np.meshgrid(x, y)

# U
plt.contourf(X, Y, U_new)
plt.colorbar(label='u')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('U')


# V
plt.contourf(X, Y, V_new)
plt.colorbar(label='v')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('V')


# P
plt.contourf(X, Y, P_new)
plt.colorbar(label='p')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('P')
plt.contour(X, Y, P_new)
plt.streamplot(X, Y, U_new, V_new)
#plt.savefig('projection.png')
plt.show()