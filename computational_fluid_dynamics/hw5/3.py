import numpy as np
import matplotlib.pyplot as plt

N = 100
x_max = np.pi
dx = x_max / N
dt = 0.01
alpha_sq = 4

x_values = np.linspace(0, x_max, N)
U = np.zeros(N)
U_prev = np.zeros(N)

U_t_initial = x_values**3 * (3 * x_values - 4 * np.pi)
U = U_t_initial * dt + 0.5 * alpha_sq * (dx ** 2) * np.sin(np.pi * x_values / x_max)

num_steps = 1000
for step in range(num_steps):
    U_next = np.zeros(N)
    for i in range(1, N - 1):
        U_next[i] = 2 * U[i] - U_prev[i] + alpha_sq * (dt**2 / dx**2) * (U[i + 1] - 2 * U[i] + U[i - 1])
        U_prev = np.copy(U)
        U = np.copy(U_next)

plt.plot(x_values, U)
plt.xlabel('x')
plt.ylabel('U(t=steady state, x)')
plt.show()
