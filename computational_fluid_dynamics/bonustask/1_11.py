import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
dx = 0.01
dy = 0.01
dt = 0.0001
Re = 100
rho = 1000
nu = 1 / Re

eps = 1e-6
eps_P = 1e-6
stop_iteration = 1e4
stop_iteration_P = 1e6

# Mesh grid
x = np.arange(0, 1 + dx, dx)
y = np.arange(0, 1 + dy, dy)
X, Y = np.meshgrid(x, y)
N, M = len(x), len(y)

# Inlet and initial conditions
U_old, V_old, P_old = np.zeros((M, N)), np.zeros((M, N)), np.zeros((M, N))
U_old[M // 2 :, : N // 5] = 1
V_old[M // 2 :, : N // 5] = 0
P_old[M // 2 :, : N // 5] = 1

# Wall conditions
U_old[0:M // 2, : N // 5] = 0
U_old[0, N // 5 :] = 0
U_old[M - 1, :] = 0

V_old[0:M // 2, : N // 5] = 0
V_old[0, N // 5 :] = 0
V_old[M - 1, :] = 0

P_old[0:M // 2, : N // 5 - 1] = P_old[0:M // 2, 1:N // 5]
P_old[0, N // 5 :] = P_old[1, N // 5 :]
P_old[M - 1, :] = P_old[M - 2, :]

U_old[:, -1] = U_old[:, -2]
V_old[:, -1] = 0
P_old[:, -1] = 0

# Simulation loop
max_val = 1
iteration = 0

while max_val > eps and iteration < stop_iteration:

    # Step 1: Solve Burgers' equation
    U_star = U_old - dt * (
    U_old * (U_old[:, 2:] - U_old[:, :-2]) / (2 * dx)
    + V_old * (U_old[2:, 1:-1] - U_old[:-2, 1:-1]) / (2 * dy)
    - nu * (
        (U_old[:, 2:] - 2 * U_old[:, 1:-1] + U_old[:, :-2]) / dx ** 2
        + (U_old[2:, 1:-1] - 2 * U_old[1:-1, :] + U_old[:-2, 1:-1]) / dy ** 2
    )
)


    V_star = V_old - dt * (
        U_old * (V_old[:, 2:] - V_old[:, :-2]) / (2 * dx)
        + V_old * (V_old[2:, :] - V_old[:-2, :]) / (2 * dy)
        - nu * (
            (V_old[:, 2:] - 2 * V_old[:, 1:-1] + V_old[:, :-2]) / dx ** 2
            + (V_old[2:, :] - 2 * V_old[1:-1, :] + V_old[:-2, :]) / dy ** 2
        )
    )

    U_star[0, N // 5 :] = 0
    U_star[M - 1, :] = 0
    U_star[0:M // 2, : N // 5] = 0
    U_star[M // 2 :, : N // 5] = 1
    U_star[:, -1] = U_star[:, -2]

    V_star[0, N // 5 :] = 0
    V_star[M - 1, :] = 0
    V_star[:, : N // 5] = 0
    V_star[:, -1] = 0

    # Step 2: Solve Poisson's equation
    P_new = np.zeros_like(P_old)
    iteration_P = 0
    max_P = 1

    while max_P > eps_P and iteration_P < stop_iteration_P:
        P_new[1:-1, 1:-1] = (
            (dy ** 2 * (P_old[1:-1, 2:] + P_old[1:-1, :-2]) + dx ** 2 * (P_old[2:, 1:-1] + P_old[:-2, 1:-1]))
            / (2 * (dx ** 2 + dy ** 2))
            - dx ** 2 * dy ** 2 * rho
            / (2 * dt * (dx ** 2 + dy ** 2))
            * (
                (U_star[1:-1, 2:] - U_star[1:-1, :-2]) / (2 * dx)
                + (V_star[2:, 1:-1] - V_star[:-2, 1:-1]) / (2 * dy)
            )
        )

        P_new[0:M // 2, : N // 5 - 1] = P_new[0:M // 2, 1:N // 5]
        P_new[M // 2 :, : N // 5] = 1
        P_new[:, -1] = 0
        P_new[0, N // 5 :] = P_new[1, N // 5 :]
        P_new[M - 1, :] = P_new[M - 2, :]

        max_P = np.max(np.abs(P_new - P_old))
        P_old[:, :] = P_new[:, :]
        iteration_P += 1

    # Step 3: Corrector
    U_new = U_star - dt / rho * (P_new[:, 2:] - P_new[:, :-2]) / (2 * dx)
    V_new = V_star - dt / rho * (P_new[2:, :] - P_new[:-2, :]) / (2 * dy)

    U_new[0:M // 2, : N // 5] = 0
    U_new[M // 2 :, : N // 5] = 1
    U_new[:, -1] = U_new[:, -2]
    U_new[0, :] = 0
    U_new[M - 1, :] = 0

    V_new[0:M // 2, : N // 5] = 0
    V_new[M // 2 :, : N // 5] = 0
    V_new[:, -1] = V_new[:, -2]
    V_new[0, :] = 0
    V_new[M - 1, :] = 0

    max_val = np.max(np.abs(U_new - U_old))
    U_old[:, :] = U_new[:, :]
    V_old[:, :] = V_new[:, :]
    iteration += 1

# Plotting
plt.figure(figsize=(15, 5))

# U
plt.subplot(131)
plt.contourf(X, Y, U_new, cmap="viridis")
plt.colorbar(label="u")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Velocity U")

# V
plt.subplot(132)
plt.contourf(X, Y, V_new, cmap="viridis")
plt.colorbar(label="v")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Velocity V")

# P
plt.subplot(133)
plt.contourf(X, Y, P_new, cmap="viridis")
plt.colorbar(label="p")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Pressure P")

plt.tight_layout()
plt.show()
