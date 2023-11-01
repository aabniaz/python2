import numpy as np
import matplotlib.pyplot as plt

xstart, xend = 0, 3
ystart, yend = 0, 3
dx = 0.1
dy = 0.1
dt = 0.001
eps = 1e-6

x = np.arange(xstart, xend + dx, dx)
y = np.arange(ystart, yend + dy, dy)
N = len(x)
M = len(y)
T = np.zeros((N, M))

T_outside = 284
T_radiator = 373

T[:, :] = T_outside
T[0, :] = T_outside
T[-1, int(0.5*M):int(2.5*M)+1] = T_radiator

convergence = 1e-5
max_iterations = 10000

for iteration in range(max_iterations):
    T_new = np.copy(T)
    for i in range(1, N-1):
        for j in range(1, M-1):
            if not (i == N-1 or (i == N and 0.5*M <= j <= 2.5*M)):
                T_new[i, j] = T[i, j] + (dt / dx**2) * (T[i+1, j] - 2*T[i, j] + T[i-1, j]) + (dt / dy**2) * (T[i, j+1] - 2*T[i, j] + T[i, j-1])
    if np.max(np.abs(T_new - T)) < convergence:
        break
    T = np.copy(T_new)

print(T)

plt.contourf(x, y, T.T, cmap='viridis')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Temperature')
plt.show()


