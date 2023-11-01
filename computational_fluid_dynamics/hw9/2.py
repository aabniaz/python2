import numpy as np
import matplotlib.pyplot as plt

nx = 101
ny = 101
dx = 1.0 / (nx - 1)
dy = 1.0 / (ny - 1)

T = np.zeros((nx, ny))

T[0, :] = 1
T[-1, :] = 0
T[:, 0] = 0
T[:, -1] = 0

max_iterations = 10000
tolerance = 1e-5
for iteration in range(max_iterations):
    max_error = 0.0
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            new_T = 0.25 * (T[i + 1, j] + T[i - 1, j] + T[i, j + 1] + T[i, j - 1])
            max_error = max(max_error, abs(new_T - T[i, j]))
            T[i, j] = new_T
    if max_error < tolerance:
        break

print(f"Converged in {iteration + 1} iterations")

plt.figure(figsize=(8, 6))
plt.contourf(np.linspace(0, 1, nx), np.linspace(0, 1, ny), T.T, cmap='viridis')
plt.colorbar(label='Temperature')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()