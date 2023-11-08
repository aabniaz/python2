import numpy as np
import matplotlib.pyplot as plt

nx = 101
ny = 101
dx = 1.0 / (nx - 1)
dy = 1.0 / (ny - 1)
nu = 0.1

u = np.zeros((nx, ny))
v = np.zeros((nx, ny))

u[int(0.1 / dy):int(0.6 / dy + 1), int(0.1 / dx):int(0.2 / dx + 1)] = 1
v[int(0.1 / dy):int(0.6 / dy + 1), int(0.1 / dx):int(0.2 / dx + 1)] = 0

nt = 100
dt = 0.01

for n in range(nt):
    un = u.copy()
    vn = v.copy()

    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            u[i, j] = (un[i, j] - un[i, j] * (dt / dx) * (un[i, j] - un[i-1, j]) -
                       vn[i, j] * (dt / dy) * (un[i, j] - un[i, j-1]) +
                       nu * (dt / dx**2) * (un[i+1, j] - 2*un[i, j] + un[i-1, j]) +
                       nu * (dt / dy**2) * (un[i, j+1] - 2*un[i, j] + un[i, j-1]))
            
            v[i, j] = (vn[i, j] - un[i, j] * (dt / dx) * (vn[i, j] - vn[i-1, j]) -
                       vn[i, j] * (dt / dy) * (vn[i, j] - vn[i, j-1]) +
                       nu * (dt / dx**2) * (vn[i+1, j] - 2*vn[i, j] + vn[i-1, j]) +
                       nu * (dt / dy**2) * (vn[i, j+1] - 2*vn[i, j] + vn[i, j-1]))


X, Y = np.meshgrid(np.linspace(0, 1, nx), np.linspace(0, 1, ny))
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, u, v)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("2D Burgers' Equation - Velocity Field")
plt.show()
