import numpy as np
import matplotlib.pyplot as plt

# Define grid parameters
nx = 50  # Number of grid points in x-direction
ny = 50  # Number of grid points in y-direction
Lx = 1.0  # Length of domain in x-direction
Ly = 1.0  # Length of domain in y-direction
dx = Lx / (nx - 1)  # Grid spacing in x-direction
dy = Ly / (ny - 1)  # Grid spacing in y-direction

# Initialize variables
u = np.zeros((ny, nx))  # Velocity component in x-direction
v = np.zeros((ny, nx))  # Velocity component in y-direction
P = np.ones((ny, nx))  # Pressure

# Set initial and boundary conditions
u[0, :] = 1  # Inlet condition: u = 1
v[0, :] = 0  # Inlet condition: v = 0
P[0, :] = 1  # Inlet condition: P = 1
u[-1, :] = 0  # Outlet condition: du/dx = 0
v[-1, :] = 0  # Outlet condition: v = 0
P[-1, :] = 0  # Outlet condition: P = 0
u[:, 0] = 0  # Wall condition: u = 0
u[:, -1] = 0  # Wall condition: u = 0
v[:, 0] = 0  # Wall condition: v = 0
v[:, -1] = 0  # Wall condition: v = 0

# Define convergence criteria
tolerance = 1e-5  # Tolerance for pressure convergence
max_iter = 1000  # Maximum number of iterations for pressure convergence

# Define fluid properties
rho = 1.0  # Density of fluid
nu = 0.1  # Kinematic viscosity

# Time-stepping loop
while True:
    # Solve Burgers equation to find u* and v*
    un = u.copy()
    vn = v.copy()
    dt = 0.01  # Time step size
    u[1:-1, 1:-1] = un[1:-1, 1:-1] - un[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) * dt / dx \
                    - vn[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) * dt / dy
    v[1:-1, 1:-1] = vn[1:-1, 1:-1] - un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) * dt / dx \
                    - vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) * dt / dy
    
    # Solve Poisson equation for pressure
   # Solve Poisson equation for pressure
    Pn = P.copy()
    for q in range(max_iter):
        P[1:-1, 1:-1] = ((P[2:, 1:-1] + P[0:-2, 1:-1]) * dy**2 + (P[1:-1, 2:] + P[1:-1, 0:-2]) * dx**2) / (2 * (dx**2 + dy**2)) \
                    - rho * dx**2 * dy**2 / (2 * (dx**2 + dy**2)) \
                    * ((u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dx) + (v[1:-1, 2:] - v[1:-1, 0:-2]) / (2 * dy)) \
                    - rho * dx**2 * (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, 0:-2]) / (2 * (dx**2 + dy**2)) \
                    - rho * dy**2 * (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[0:-2, 1:-1]) / (2 * (dx**2 + dy**2))
    
    # Check convergence
    if np.abs(P - Pn).max() < tolerance:
        break

# Calculate corrector for u and v
    u[1:-1, 1:-1] = un[1:-1, 1:-1] - dt / dx * (P[1:-1, 2:] - P[1:-1, 0:-2])
    v[1:-1, 1:-1] = vn[1:-1, 1:-1] - dt / dy * (P[2:, 1:-1] - P[0:-2, 1:-1])

# Check for steady state
    if np.abs(u - un).max() < tolerance and np.abs(v - vn).max() < tolerance:
        break

# Plot the results
plt.figure(figsize=(10, 5))
plt.contourf(u, cmap='jet')
plt.colorbar()
plt.title('Velocity Component in X-Direction')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()