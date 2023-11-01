import numpy as np
import matplotlib.pyplot as plt

N = 100  
x_max = np.pi
dx = x_max / N  
dt = 0.01  
alpha_sq = 5
x_values = np.linspace(0, x_max, N)
U = np.zeros(N)
U_prev = np.zeros(N)

U = x_values * np.sin(np.pi * x_values)

num_steps = 1000
for step in range(num_steps):
    for i in range(1, N - 1):
        U_next = 5 * (dt ** 2 / dx ** 2) * (U[i + 1] - 2 * U[i] + U[i - 1]) + 2 * U[i] - U_prev[i]
        U_prev[i] = U[i]
        U[i] = U_next

plt.plot(x_values, U)
plt.xlabel('x')
plt.ylabel('U(t=steady state, x)')
plt.show()
