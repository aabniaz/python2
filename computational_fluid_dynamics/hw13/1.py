import numpy as np
import matplotlib.pyplot as plt

nx, ny = 41, 41  
dx, dy = 2 / (nx - 1), 2 / (ny - 1) 
nu = 0.1  
dt = 0.001  
nit = 50 

u = np.ones((ny, nx))
v = np.zeros((ny, nx))
p = np.ones((ny, nx))
b = np.zeros((ny, nx))

u[0, :] = 1  # Inlet
u[-1, :] = 1  # Outlet
u[:, 0] = 1  # Left wall
u[:, -1] = 1  # Right wall

v[0, :] = 0  # Inlet
v[-1, :] = 0  # Outlet
v[:, 0] = 0  # Left wall
v[:, -1] = 0  # Right wall

for n in range(300):
    # Step 1: Burgers equation to find u* and v*
    un = u.copy()
    vn = v.copy()

    u[1:-1, 1:-1] = (un[1:-1, 1:-1] -
                    dt / dx * un[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) -
                    dt / dy * vn[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) +
                    nu * (dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                          dt / dy**2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])))

    v[1:-1, 1:-1] = (vn[1:-1, 1:-1] -
                    dt / dx * un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) -
                    dt / dy * vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) +
                    nu * (dt / dx**2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) +
                          dt / dy**2 * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1])))

    # Step 2: Solve Poisson equation for pressure using Jacobi method
    for q in range(nit):
        pn = p.copy()
        p[1:-1, 1:-1] = ((dx**2 + dy**2) / (2 * (dx**2 + dy**2)) *
                        ((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy**2 +
                         (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx**2) /
                        (2 * (dx**2 + dy**2)) -
                        dx**2 * dy**2 / (2 * (dx**2 + dy**2)) * b[1:-1, 1:-1])

        # Boundary conditions for pressure
        p[:, -1] = p[:, -2]  # dp/dx = 0 at x = 2
        p[0, :] = p[1, :]    # dp/dy = 0 at y = 0
        p[:, 0] = p[:, 1]    # dp/dx = 0 at x = 0
        p[-1, :] = 0         # p = 0 at y = 2

    # Step 3: Apply pressure correction
    u[1:-1, 1:-1] -= dt / dx * (p[1:-1, 2:] - p[1:-1, 0:-2]) / (2 * dx)
    v[1:-1, 1:-1] -= dt / dy * (p[2:, 1:-1] - p[0:-2, 1:-1]) / (2 * dy)

    # Boundary conditions for velocity after pressure correction
    u[0, :] = 1  # Inlet
    u[-1, :] = 1  # Outlet
    u[:, 0] = 1  # Left wall
    u[:, -1] = 1  # Right wall

    v[0, :] = 0  # Inlet
    v[-1, :] = 0  # Outlet
    v[:, 0] = 0  # Left wall
    v[:, -1] = 0  # Right wall

x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
X, Y = np.meshgrid(x, y)

# Contour plot for u
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.contourf(X, Y, u, cmap='viridis', levels=20)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour plot for u')

# Contour plot for v
plt.subplot(132)
plt.contourf(X, Y, v, cmap='viridis', levels=20)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour plot for v')

# Contour plot for pressure
plt.subplot(133)
plt.contourf(X, Y, p, cmap='viridis', levels=20)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour plot for pressure')

plt.tight_layout()
plt.show()




# import numpy as np
# import matplotlib.pyplot as plt

# nx, ny = 41, 41
# dx, dy = 2 / (nx - 1), 2 / (ny - 1)

# nu = 0.1
# dt = 0.001
# nit = 50

# u = np.zeros((ny, nx))
# v = np.zeros((ny, nx))

# x = np.linspace(0, 1, nx)
# y = np.linspace(0, 1, ny)
# X, Y = np.meshgrid(x, y)
# p = np.linspace(0, 1, ny).reshape(-1, 1) + 0.1 * np.random.rand(ny, nx)  # Modified initialization for pressure

# # Initialize auxiliary variable b
# b = np.zeros((ny, nx))

# # Initial conditions for velocity fields
# u[:, :] = np.cos(np.pi * Y)  # Removed the shining effect
# v[:, :] = np.sin(np.pi * X)

# # Boundary conditions for velocity fields
# u[0, :] = 1  # Inlet
# u[-1, :] = 1  # Outlet
# u[:, 0] = 1  # Left wall
# u[:, -1] = 1  # Right wall

# v[0, :] = 0  # Inlet
# v[-1, :] = 0  # Outlet
# v[:, 0] = 0  # Left wall
# v[:, -1] = 0  # Right wall

# # Time-stepping loop
# for n in range(300):
#     # Step 1: Burgers equation to find u* and v*
#     un = u.copy()
#     vn = v.copy()

#     u[1:-1, 1:-1] = (un[1:-1, 1:-1] -
#                     dt / dx * un[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) -
#                     dt / dy * vn[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) +
#                     nu * (dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
#                           dt / dy**2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])))

#     v[1:-1, 1:-1] = (vn[1:-1, 1:-1] -
#                     dt / dx * un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) -
#                     dt / dy * vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) +
#                     nu * (dt / dx**2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) +
#                           dt / dy**2 * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1])))

#     # Step 2: Solve Poisson equation for pressure using Jacobi method
#     for q in range(nit):
#         pn = p.copy()
#         p[1:-1, 1:-1] = ((dx**2 + dy**2) / (2 * (dx**2 + dy**2)) *
#                         ((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy**2 +
#                          (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx**2) /
#                         (2 * (dx**2 + dy**2)) -
#                         dx**2 * dy**2 / (2 * (dx**2 + dy**2)) * b[1:-1, 1:-1])

#         # Boundary conditions for pressure
#         p[:, -1] = p[:, -2]  # dp/dx = 0 at x = 2
#         p[0, :] = p[1, :]    # dp/dy = 0 at y = 0
#         p[:, 0] = p[:, 1]    # dp/dx = 0 at x = 0
#         p[-1, :] = 0         # p = 0 at y = 2

#     # Step 3: Apply pressure correction
#     u[1:-1, 1:-1] -= dt / dx * (p[1:-1, 2:] - p[1:-1, 0:-2]) / (2 * dx)
#     v[1:-1, 1:-1] -= dt / dy * (p[2:, 1:-1] - p[0:-2, 1:-1]) / (2 * dy)

#     # Boundary conditions for velocity after pressure correction
#     u[0, :] = 1  # Inlet
#     u[-1, :] = 1  # Outlet
#     u[:, 0] = 1  # Left wall
#     u[:, -1] = 1  # Right wall

#     v[0, :] = 0  # Inlet
#     v[-1, :] = 0  # Outlet
#     v[:, 0] = 0  # Left wall
#     v[:, -1] = 0  # Right wall

# # Contour plot for u
# plt.figure(figsize=(12, 4))
# plt.subplot(131)
# plt.contourf(X, Y, u, cmap='viridis', levels=20)
# plt.colorbar()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Contour plot for u')

# # Contour plot for v
# plt.subplot(132)
# plt.contourf(X, Y, v, cmap='viridis', levels=20)
# plt.colorbar()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Contour plot for v')

# # Contour plot for pressure
# plt.subplot(133)
# plt.contourf(X, Y, p, cmap='viridis', levels=20)
# plt.colorbar()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Contour plot for pressure')

# plt.tight_layout()
# plt.show()
