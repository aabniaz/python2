import numpy as np
import matplotlib.pyplot as plt

dx = 0.027
dy = 0.027
dt = 0.0001
Re = 1
dens = 1
visc = 1/Re

eps = 1e-6
eps_P = 1e-6
stop_it = 1e4
dstop_it_P = 1e6

x = np.arange(0, dx+1, dx)
y = np.arange(0, dy+1, dy)
N = len(x)
M = len(y)

U_init = np.zeros((M, N))
U_star = np.zeros((M, N))
U_corr = np.zeros((M, N))
V_init = np.zeros((M, N))
V_star = np.zeros((M, N))
V_corr = np.zeros((M, N))
P_init = np.zeros((M, N))
P_corr = np.zeros((M, N))

# at t=0
U_init[:, :] = 0
V_init[:, :] = 0
P_init[:, :] = 0

# bound. cond.
U_init[0, :] = 0 # Bottom
U_init[M-1, :] = 1 # Top
U_init[:, 0] = 0 # Left
U_init[:, N-1] = 0 # Right
V_init[0, :] = 0
V_init[M-1, :] = 0
V_init[:, 0] = 0
V_init[:, N-1] = 0
P_init[0, :] = P_init[1, :]
P_init[M-1, :] = 1
P_init[:, 0] = P_init[:, 1]
P_init[:, N-1] = P_init[:, N-2]
maximum = 1
iteration = 0

while maximum > eps and iteration < stop_it:
    U_star[1:-1, 1:-1] = U_init[1:-1, 1:-1] - dt*(U_init[1:-1, 1:-1]*(U_init[1:-1, 2:] - U_init[1:-1, 0:-2])/(2*dx) \
    + V_init[1:-1, 1:-1]*(U_init[2:, 1:-1] - U_init[0:-2, 1:-1])/(2*dy) - visc*((U_init[1:-1, 2:] - 2*U_init[1:-1, 1:-1] + U_init[1:-1, 0:-2])/dx**2 \
    + (U_init[2:, 1:-1] - 2*U_init[1:-1, 1:-1] + U_init[0:-2, 1:-1])/dy**2))

    V_star[1:-1, 1:-1] = V_init[1:-1, 1:-1] - dt*(U_init[1:-1, 1:-1]*(V_init[1:-1, 2:] - V_init[1:-1, 0:-2])/(2*dx) \
    + V_init[1:-1, 1:-1]*(V_init[2:, 1:-1] - V_init[0:-2, 1:-1])/(2*dy) - visc*((V_init[1:-1, 2:] - 2*V_init[1:-1, 1:-1] + V_init[1:-1, 0:-2])/dx**2 \
    + (V_init[2:, 1:-1] - 2*V_init[1:-1, 1:-1] + V_init[0:-2, 1:-1])/dy**2))

    U_star[0, :] = 0
    U_star[M-1, :] = 1
    U_star[:, 0] = 0
    U_star[:, N-1] = 0
    V_star[0, :] = 0
    V_star[M-1, :] = 0  
    V_star[:, 0] = 0
    V_star[:, N-1] = 0
    maximum_P = 1
    iteration_P = 0

    while maximum_P > eps_P and iteration_P < dstop_it_P:
        P_corr[1:-1, 1:-1] = (dy**2*(P_init[1:-1, 2:] + P_init[1:-1, 0:-2]) + dx**2*(P_init[2:, 1:-1] + P_init[0:-2, 1:-1]))/(2*(dx**2 + dy**2)) \
    - dx**2*dy**2*dens/(2*dt*(dx**2 + dy**2)) * ((U_star[1:-1, 2:] - U_star[1:-1, 0:-2])/(2*dx) \
    + (V_star[2:, 1:-1] - V_star[0:-2, 1:-1])/(2*dy))

        P_corr[0, :] = P_corr[1, :]
        P_corr[M-1, :] = 0
        P_corr[:, 0] = P_corr[:, 1]
        P_corr[:, N-1] = P_corr[:, N-2]
        maximum_P = np.max(np.abs(P_corr - P_init))
        P_init[:, :] = P_corr[:, :]
        iteration_P += 1

    U_corr[1:-1, 1:-1] = U_star[1:-1, 1:-1] - dt/dens * (P_corr[1:-1, 2:] - P_corr[1:-1, 0:-2])/(2*dx)
    V_corr[1:-1, 1:-1] = V_star[1:-1, 1:-1] - dt/dens * (P_corr[2:, 1:-1] - P_corr[0:-2, 1:-1])/(2*dy)
    U_corr[0, :] = 0
    U_corr[M-1, :] = 1
    U_corr[:, 0] = 0
    U_corr[:, N-1] = 0
    V_corr[0, :] = 0
    V_corr[M-1, :] = 0
    V_corr[:, 0] = 0
    V_corr[:, N-1] = 0
    maximum = np.max(np.abs(U_corr - U_init))
    U_init[:, :] = U_corr[:, :]
    V_init[:, :] = V_corr[:, :]
# maximum = 1
    iteration += 1

X, Y = np.meshgrid(x, y)

plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.contourf(X, Y, U_corr, cmap='viridis', levels=20)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('u')

plt.subplot(132)
plt.contourf(X, Y, V_corr, cmap='viridis', levels=20)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('v')

plt.subplot(133)
plt.contourf(X, Y, P_corr, cmap='viridis', levels=20)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('p')
plt.contour(X, Y, P_corr)
plt.streamplot(X, Y, U_corr, V_corr)

plt.tight_layout()
plt.savefig('hw14.png')
plt.show()

center = int(M / 2)
plt.plot(U_corr[:, center], x)
plt.title('profile of u at the center')
plt.grid(True)
plt.show()