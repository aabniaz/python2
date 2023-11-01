import numpy as np
import matplotlib.pyplot as plt

delta_x = 0.1
delta_t = 0.001 
x_points = int(1 / delta_x) + 1  
t_steps = 100 

y = np.zeros((t_steps + 1, x_points))
x = np.arange(0, 1.1, delta_x)

y[0, :] = 0  
y[:, 0] = 1 
y[:, -1] = 0  

a = 1
stability_condition = (a**2) * (delta_t / (delta_x**2))
print("Stability condition (a^2 * delta_t / delta_x^2):", stability_condition)

for i in range(t_steps):
    for j in range(1, x_points - 1):
        y[i + 1][j] = y[i, j] + stability_condition * (y[i, j + 1] - 2 * y[i, j] + y[i, j - 1])

plt.plot(np.arange(0, x_points) * delta_x, y[-1, :])
plt.xlabel('x')
plt.ylabel('U(x) at t=1')
plt.show()
