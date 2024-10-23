# import numpy as np
# import matplotlib.pyplot as plt

# # Parameters
# nx = 40
# ny = 30
# xmin = 0
# xmax = 1.5
# ymin = 0
# ymax = 1
# dt = 0.001
# nstep = 5050
# mu = 0.001
# un = 1
# us = 0
# ve = 0
# vw = 0
# maxit = 650
# pit = 100
# plotvorticity = 1

# # Initializing
# time = 0.0
# dx = (xmax - xmin) / nx
# dy = (ymax - ymin) / ny
# X, Y = np.meshgrid(np.arange(xmin, xmax + dx, dx), np.arange(ymin, ymax + dy, dy))
# u = np.zeros((nx + 1, ny + 2))
# v = np.zeros((nx + 2, ny + 1))
# p = np.zeros((nx + 2, ny + 2))
# pp = np.zeros((nx + 1, ny + 1))
# ut = np.zeros((nx + 1, ny + 2))
# vt = np.zeros((nx + 2, ny + 1))
# uu = np.zeros((nx + 1, ny + 1))
# vv = np.zeros((nx + 1, ny + 1))
# if plotvorticity == 1:
#     w = np.zeros((nx + 1, ny + 1))

# # Main time-stepping loop
# for is in range(1, nstep + 1):
#     # Enforcing b.c by interpolation
#     u[1:nx + 1, 0] = 2 * us - u[1:nx + 1, 1]
#     u[1:nx + 1, ny + 1] = 2 * un - u[1:nx + 1, ny]
#     v[0, 1:ny + 1] = 2 * vw - v[1, 1:ny + 1]
#     v[nx + 1, 1:ny + 1] = 2 * ve - v[nx, 1:ny + 1]

#     # Temporary u-velocity
#     ut[1:nx, 1:ny + 1] = u[1:nx, 1:ny + 1] + dt * (
#             (-0.25) * (((u[2:nx + 1, 1:ny + 1] + u[1:nx, 1:ny + 1]) ** 2 - (u[1:nx, 1:ny + 1] + u[0:nx - 1, 1:ny + 1]) ** 2) / dx
#                        + ((u[1:nx, 2:ny + 2] + u[1:nx, 1:ny + 1]) * (v[2:nx + 1, 1:ny + 1] + v[1:nx, 1:ny + 1])
#                           - (u[1:nx, 1:ny + 1] + u[1:nx, 0:ny]) * (v[2:nx + 1, 0:ny] + v[1:nx, 0:ny])) / dy)
#             + mu * ((u[2:nx + 1, 1:ny + 1] - 2 * u[1:nx, 1:ny + 1] + u[0:nx - 1, 1:ny + 1]) / dx ** 2
#                     + (u[1:nx, 2:ny + 2] - 2 * u[1:nx, 1:ny + 1] + u[1:nx, 0:ny]) / dy ** 2))

#     # Temporary v-velocity
#     vt[1:nx + 1, 1:ny] = v[1:nx + 1, 1:ny] + dt * (
#             (-0.25) * (((u[1:nx, 2:ny + 1] + u[1:nx, 1:ny]) * (v[2:nx + 1, 1:ny] + v[1:nx, 1:ny])
#                         - (u[0:nx - 1, 2:ny + 1] + u[0:nx - 1, 1:ny]) * (v[1:nx, 1:ny] + v[0:nx - 1, 1:ny])) / dx
#                        + ((v[1:nx, 1:ny] + v[1:nx, 0:ny - 1]) ** 2 - (v[1:nx, 1:ny] + v[1:nx, 2:ny + 1]) ** 2) / dy)
#             + mu * ((v[2:nx + 1, 1:ny] - 2 * v[1:nx, 1:ny] + v[0:nx - 1, 1:ny]) / dx ** 2
#                     + (v[1:nx, 2:ny + 1] + -2 * v[1:nx, 1:ny] + v[1:nx, 0:ny - 1]) / dy ** 2))

#     pt = p.copy()
#     for it in range(maxit):
#         # Neumann b.c for pressure
#         pt[0, :] = pt[1, :]
#         pt[nx + 1, :] = pt[nx, :]
#         pt[:, 0] = pt[:, 1]
#         pt[:, ny + 1] = pt[:, ny]

#         pt[1:nx + 1, 1:ny + 1] = (0.5 / (dx ** 2 + dy ** 2)) * (
#                 (dy ** 2) * (pt[2:nx + 2, 1:ny + 1] + pt[0:nx, 1:ny + 1])
#                 + (dx ** 2) * (pt[1:nx + 1, 2:ny + 2] + pt[1:nx + 1, 0:ny])
#                 - (dx * dy / dt) * (dy * (ut[1:nx + 1, 1:ny + 1] - ut[0:nx, 1:ny + 1])
#                                     + dx * (vt[1:nx + 1, 1:ny + 1] - vt[1:nx + 1, 0:ny])))
#         Er = np.max(np.abs(pt - p))
#         p = pt.copy()
#         if Er < 1e-6:
#             break

#     # Correct the velocity
#     u[1:nx, 1:ny + 1] = ut[1:nx, 1:ny + 1] - (dt / dx) * (p[2:nx + 1, 1:ny + 1] - p[1:nx, 1:ny + 1])
#     v[1:nx + 1, 1:ny] = vt[1:nx + 1, 1:ny] - (dt / dy) * (p[1:nx + 1, 2:ny + 1] - p[1:nx + 1, 1:ny])

#     time = time + dt

#     # Plot the results
#     if is == pit * int(is / pit):
#         uu[0:nx + 1, 0:ny + 1] = 0.5 * (u[0:nx + 1, 1:ny + 2] + u[0:nx + 1, 0:ny + 1])
#         vv[0:nx + 1, 0:ny + 1] = 0.5 * (v[1:nx + 2, 0:ny + 1] + v[0:nx + 1, 0:ny + 1])
#         pp = 0.5 * (p[0:nx + 1, 0:ny + 1] + p[1:nx + 2, 1:ny + 2])

#         plt.figure()
#         plt.pcolor(X, Y, np.flipud(np.rot90(pp)), alpha=0.5, edgecolors='k', linewidths=0.5)
#         plt.quiver(X, Y, np.flipud(np.rot90(uu)), np.flipud(np.rot90(vv)), scale=2, color='black')
#         plt.title(f'Time: {time}')
#         if plotvorticity == 1:
#             w[0:nx + 1, 0:ny + 1] = (u[0:nx + 1, 1:ny + 2] - u[0:nx + 1, 0:ny + 1]) / (2 * dx) \
#                                      + (v[0:nx + 1, 0:ny + 1] - v[1:nx + 2, 0:ny + 1]) / (2 * dy)
#             plt.contour(X, Y, np.flipud(np.rot90(w)), 10)

#         plt.axis('equal')
#         plt.pause(0.005)
#         plt.draw()

# plt.show()
