import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

delta_x = 0.1
delta_t = 0.01

x = np.arange(0, 1.1, delta_x)
t = np.arange(0, 1.1, delta_t)
y = np.zeros((len(t), len(x)))  

y[0, :] = 0 
y[:, 0] = 1 
y[:, -1] = 0  
u = 1

for i in range(len(t)-1):
    for j in range(1, len(x)-1):
        y[i, j + 1] = -u * delta_t / delta_x * (y[i, j] - y[i - 1, j]) + y[i, j]
print(y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
T, X = np.meshgrid(x, t)  
surf = ax.plot_surface(T, X, y, cmap='viridis')
fig.colorbar(surf)
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('T')
plt.show()
