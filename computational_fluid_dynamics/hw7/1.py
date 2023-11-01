import numpy as np
import matplotlib.pyplot as plt

N = 10  
M = 10  
Lx = 0.1  
Ly = 0.1  
dx = Lx / N  
dy = Ly / M  
dt = min(dx**2, dy**2) / 4  

x = np.linspace(0, Lx, N+1)
y = np.linspace(0, Ly, M+1)

T = np.zeros((N+1, M+1))

T[:, 0] = 0  
T[:, 1] = 0  
T[0, :] = 1  
T[1, :] = 0  

eps = 1e-5
max = 10000

for it in range(max):
    T_new = np.copy(T)
    for i in range(1, N):
        for j in range(1, M):
            T_new[i, j] = T[i, j] + (dt / dx**2) * (T[i+1, j] - 2*T[i, j] + T[i-1, j] + T[i, j+1] - 2*T[i, j] + T[i, j-1])
    if np.max(np.abs(T_new - T)) < eps:
        break
    T = np.copy(T_new)
print(T)
#print(f'Steady state reached after {it+1} iterations.')

plt.contourf(x, y, T.T, cmap='viridis')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Temperature')
plt.show()