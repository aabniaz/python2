import numpy as np
import matplotlib.pyplot as plt

u = -1
alpha = 1
dx = 0.1
dt = 0.00001
eps = 0.0001

L = 1.0
Nx = int(L / dx) + 1
Nt = 5000
x = np.linspace(0, 1, Nx)
T = np.zeros((Nt, Nx))

T[0, :] = 0
T[:, 0] = 1
T[:, -1] = 2

CFL = (u * dt) / (dx ** 2)
assert CFL <= 0.5, "CFL condition not satisfied"

for n in range(Nt - 1):
    for i in range(1, Nx - 1):
        T[n + 1, i] = T[n, i] + dt * ((alpha**2 / dx**2) * (T[n, i + 1] - 2 * T[n, i] + T[n, i - 1]) - u / dx * (T[n, i] - T[n, i - 1]))

x_values = np.linspace(0, 1, Nx)
U_steady_state = T[-1, :]

plt.plot(x_values, U_steady_state)
plt.xlabel('x')
plt.ylabel('U(t=steady state, x)')
plt.show()
    