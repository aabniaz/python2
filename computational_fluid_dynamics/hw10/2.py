import numpy as np
import matplotlib.pyplot as plt

c = 1
L = 1  
T = 1  # Changed to solve until T=1
dx = 0.1  
dt = 0.05  
xs = int(L / dx) + 1
ts = int(T / dt) + 1

x_v = np.linspace(0, L, xs)
t_v = np.linspace(0, T, ts)
u = np.zeros((ts, xs))

u[0, :] = 0  
u[:, 0] = 1  
u[:, -1] = 0  

for n in range(1, ts - 1):  # Start from 1
    for j in range(1, xs - 1):
        u[n + 1, j] = u[n - 1, j] - c * (dt / dx) * (u[n, j + 1] - u[n, j - 1])

x = 0.1
x_index = int(x / dx)
plt.plot(t_v, u[:, x_index])  
plt.xlabel('Time')
plt.ylabel('U at x = 0.1')
plt.show()