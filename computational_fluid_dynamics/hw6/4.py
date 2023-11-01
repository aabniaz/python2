import numpy as np
import matplotlib.pyplot as plt

N = 100  
M = 5000  
L = 1.0  
dx = L / (N - 1)  
dt = 0.0001  
Reynolds_numbers = [5495, 1800, 1000]  

x = np.linspace(0, L, N)  
u_solutions = []

u_initial = np.zeros(N)
u_initial[0] = 1.0  
u_solutions.append(u_initial.copy())

def scheme(u_prev, dx, dt, Re):
    u_next = u_prev.copy()
    for i in range(1, N - 1):
        u_next[i] = u_prev[i] - (u_prev[i] * dt / (2 * dx)) * (u_prev[i + 1] - u_prev[i - 1]) \
                    + (dt / Re) * ((u_prev[i + 1] - 2 * u_prev[i] + u_prev[i - 1]) / (dx ** 2))
    return u_next

for Re in Reynolds_numbers:
    u = u_initial.copy()
    for m in range(M):
        u = scheme(u, dx, dt, Re)
        if m > 0 and np.max(np.abs(u - u_solutions[-1])) < 1e-6:
            break
    u_solutions.append(u)

plt.figure(figsize=(12, 8))
for i, Re in enumerate(Reynolds_numbers):
    plt.subplot(3, 1, i + 1)
    plt.plot(x, u_solutions[i], label=f'Re = {Re}')
    plt.xlabel('x')
    plt.ylabel('u')
    plt.legend()
    plt.title(f'When Reynolds Number Re is = {Re}')

plt.tight_layout()
plt.show()
