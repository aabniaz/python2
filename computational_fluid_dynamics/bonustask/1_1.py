import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
dy = 0.01
dt = 0.0001
Re = 100
rho = 1000
nu = 1/Re
eps = 1e-6
eps_P = 1e-6
stop_iteration = 1e4
stop_iteration_P = 1e6

#grid
x = np.arange(0, 1 + dx, dx)
y = np.arange(0, 1 + dy, dy)
N = len(x)
M = len(y)

#initial cond
U = np.zeros((M, N))
V = np.zeros((M, N))
P = np.zeros((M, N))

#inlet cond
U[M//2:, 0:N//2] = 1
V[M//2:, 0:N//2] = 0
P[M//2:, 0:N//2] = 1

#wall cond
U[0:M//2, :] = 0
V[0:M//2, :] = 0
U[:, N-1] = U[:, N-2]
V[:, N-1] = 0

#outlet cond
U[:, N-1] = U[:, N-2]
V[:, N-1] = 0
P[:, N-1] = 0

max_U = 1
iter_U = 0

while max_U > eps and iter_U < stop_iteration:
    #U and V using the burgers eq
    U_s = U - dt * (
        U * (U[:, 1:] - U[:, :-1]) / (2 * dx) +
        V * (U[1:, :] - U[:-1, :]) / (2 * dy) -
        nu * (np.gradient(np.gradient(U, axis=0), axis=0) + np.gradient(np.gradient(U, axis=1), axis=1))
    )
    
    V_s = V - dt * (
        U * (V[:, 1:] - V[:, :-1]) / (2 * dx) +
        V * (V[1:, :] - V[:-1, :]) / (2 * dy) -
        nu * (np.gradient(np.gradient(V, axis=0), axis=0) + np.gradient(np.gradient(V, axis=1), axis=1))
    )

    #boundary cond
    U_s[0:M//2, :] = 0
    U_s[:, N-1] = U_s[:, N-2]
    V_s[0:M//2, :] = 0
    V_s[:, N-1] = 0

    max_P = 1
    iter_P = 0

    #poisson eq for p
    while max_P > eps_P and iter_P < stop_iteration_P:
        P_new = (dy**2 * (np.roll(P, -1, axis=1) + np.roll(P, 1, axis=1)) +
                 dx**2 * (np.roll(P, -1, axis=0) + np.roll(P, 1, axis=0))) / (2 * (dx**2 + dy**2)) \
                - dx**2 * dy**2 * rho / (2 * dt * (dx**2 + dy**2)) * (
                    (np.roll(U_s, -1, axis=1) - np.roll(U_s, 1, axis=1)) / (2 * dx) +
                    (np.roll(V_s, -1, axis=0) - np.roll(V_s, 1, axis=0)) / (2 * dy)
                )

        #boundary cond for p
        P_new[0:M//2, :-1] = P_new[0:M//2, 1:]
        P_new[M-1, :] = P_new[M-2, :]
        P_new[:, N-1] = 0

        max_P = np.max(np.abs(P_new - P))
        P = P_new.copy()
        iter_P += 1

    #corrector
    U_new = U_s - dt / rho * (np.roll(P, -1, axis=1) - np.roll(P, 1, axis=1)) / (2 * dx)
    V_new = V_s - dt / rho * (np.roll(P, -1, axis=0) - np.roll(P, 1, axis=0)) / (2 * dy)

    #boundary cond for velocity
    U_new[0:M//2, :] = 0
    U_new[:, N-1] = U_new[:, N-2]
    U_new[M//2, :] = 0
    U_new[M//2:, 0:N//2] = 1
    V_new[0:M//2, :] = 0
    V_new[:, N-1] = 0

    #max change in U
    max_U = np.max(np.abs(U_new - U))
    U = U_new.copy()
    V = V_new.copy()
    iter_U += 1

X, Y = np.meshgrid(x, y)

#velocity U
plt.figure()
plt.contourf(X, Y, U, cmap='viridis')
plt.colorbar(label='u')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Velocity U')

#velocity V
plt.figure()
plt.contourf(X, Y, V, cmap='viridis')
plt.colorbar(label='v')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Velocity V')

#pressure P
plt.figure()
plt.contourf(X, Y, P, cmap='viridis')
plt.colorbar(label='p')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Pressure P')

plt.figure()
plt.streamplot(X, Y, U, V, color='black')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Streamlines')
plt.savefig('streamlines.png')  
plt.show()