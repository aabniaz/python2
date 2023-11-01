"""import random
num, guess_num = random.randint(1, 10), 0
while num != guess_num:
    guess_num = int(input("Guess it correct!: "))
print('Well guessed!')"""


import numpy as np
import matplotlib.pyplot as plt

L = 1.0
Nx = 100
Nt = 5000
dx = L / (Nx - 1)
dt = 0.00001
alpha = 1.0
u = 1.0

T = np.zeros((Nt, Nx))
T[0, :] = 0.0
T[:, 0] = 0.0
T[:, -1] = 0.0

CFL = (u * dt) / (dx ** 2)
assert CFL <= 0.5, "condition not satisfied"

for n in range(Nt - 1):
    for i in range(1, Nx - 1):
        T[n + 1, i] = T[n, i] + dt * ((alpha * alpha / dx**2) * (T[n, i + 1] - 2 * T[n, i] + T[n, i - 1]) - (u / dx) * (T[n, i] - T[n, i - 1]))

eps = 1e-5
steady_state_index = -1
for n in range(Nt - 1):
    if np.max(np.abs(T[n + 1, :] - T[n, :])) < eps:
        steady_state_index = n
        break

x_values = np.arange(0, L+dx, dx)
U_steady_state = T[steady_state_index, :]

plt.plot(x_values, U_steady_state)
plt.xlabel('x')
plt.ylabel('U(t=steady state, x)')
plt.show()
