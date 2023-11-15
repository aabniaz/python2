import numpy as np
import matplotlib.pyplot as plt

def lax_wendroff(c, Lx, Ly, T, dx, dy, dt):
    xs = int(Lx / dx) + 1
    ys = int(Ly / dy) + 1
    ts = int(T / dt) + 1

    x_v = np.linspace(0, Lx, xs)
    y_v = np.linspace(0, Ly, ys)
    t_v = np.linspace(0, T, ts)
    u = np.zeros((ts, xs, ys))

    u[0, :, :] = 0 
    u[:, 0, :] = 1  
    u[:, -1, :] = 0  

    for n in range(ts - 1):
        for i in range(1, xs - 1):
            for j in range(1, ys - 1):
                u[n + 1, i, j] = u[n, i, j] - c * dt / (2 * dx) * (u[n, i + 1, j] - u[n, i - 1, j]) + \
                                 c**2 * dt**2 / (2 * dx**2) * (u[n, i + 1, j] - 2 * u[n, i, j] + u[n, i - 1, j]) + \
                                 - c * dt / (2 * dy) * (u[n, i, j + 1] - u[n, i, j - 1]) + \
                                 c**2 * dt**2 / (2 * dy**2) * (u[n, i, j + 1] - 2 * u[n, i, j] + u[n, i, j - 1])

    return x_v, y_v, t_v, u

def plott(x_v, y_v, u_slice, target_y):
    y_index = np.abs(y_v - target_y).argmin()
    plt.figure()
    plt.plot(x_v, u_slice[:, y_index], label=f"Y = {target_y:.2f}")
    plt.xlabel('X')
    plt.ylabel('U')
    plt.legend()
    plt.show()

c = 1
Lx = Ly = 1
T = 10
dx = dy = 0.1
dt = 0.05

x_v, y_v, t_v, u = lax_wendroff(c, Lx, Ly, T, dx, dy, dt)
time_slice = 50
target_y = 0.5  
plott(x_v, y_v, u[time_slice, :, :], target_y)