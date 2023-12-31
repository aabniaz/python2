import numpy as np
import matplotlib.pyplot as plt

c = 1
L = 1  
T = 10  
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

for n in range(ts - 1):
    for j in range(1, xs - 1):
        u[n + 1, j] = 0.5 * (u[n, j + 1] + u[n, j - 1]) - 0.5 * c * dt / dx * (u[n, j + 1] - u[n, j - 1])

x = 0.1
x_index = int(x / dx)
plt.plot(u[n,:])  
plt.ylabel('Time')
plt.xlabel('U')
plt.show()