import numpy as np
import matplotlib.pyplot as plt

# Parameters
c = 1
L = 1  # Length of the x domain
T = 10  # Maximum time
dx = 0.1  # Spatial step
dt = 0.05  # Temporal step
x_steps = int(L / dx) + 1
t_steps = int(T / dt) + 1

# Grid initialization
x_values = np.linspace(0, L, x_steps)
t_values = np.linspace(0, T, t_steps)
u = np.zeros((t_steps, x_steps))

# Initial conditions
u[0, :] = 0  # u(t=0,x)=0
u[:, 0] = 1  # u(t,x=0)=1
u[:, -1] = 0  # u(t,x=1)=0

# Lax method
for n in range(t_steps - 1):
    for i in range(1, x_steps - 1):
        u[n + 1, i] = 0.5 * (u[n, i + 1] + u[n, i - 1]) - 0.5 * c * dt / dx * (u[n, i + 1] - u[n, i - 1])

# Plotting
X, T = np.meshgrid(x_values, t_values)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Time')
ax.set_zlabel('U')
ax.set_title('Solution of the Wave Equation using Lax method')
plt.show()
