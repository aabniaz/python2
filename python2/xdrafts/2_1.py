"""import numpy as np
import matplotlib.pyplot as plt

alpha = 1  
L = 1
N = 100  
M = 1000 
dx = L / (N - 1)  

dt = 0.9 * (dx ** 2) / (4 * alpha)  

x = np.linspace(0, L, N)
t = np.linspace(0, dt * M, M)
T = np.zeros((M, N))
T[0, :] = 0
T[:, 0] = 1  
T[:, 1] = 0  

for i in range(M - 1):
    for j in range(1, N - 1):
        T[i, j + 1] = T[i, j] + alpha * (dt / dx ** 2) * (T[i + 1, j] - 2 * T[i, j] + T[i - 1, j])
print(T)"""

""" plt.figure(figsize=(10, 6))
plt.imshow(T, extent=[0, L, 0, dt * M], origin='lower', aspect='auto', cmap='hot')
plt.colorbar(label='Temperature')
plt.xlabel('x')
plt.ylabel('Time')
plt.title('Numerical Solution of the Heat Equation')
plt.show()"""

