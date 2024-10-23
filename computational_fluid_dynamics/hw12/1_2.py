import numpy as np
import matplotlib.pyplot as plt
import timeit

start_x, end_x = 0, 1
dx, dt = 0.001, 0.001
eps = 1e-6
u = 1
N = int((end_x - start_x)/ dx+ 1)
stop_iteration = int(1e6)
x = np.linspace(start_x, end_x, N)
U_old, U_new = np.zeros(N), np.zeros(N)

def find_absolute_max():
    return np.max(np.abs(U_new - U_old))

def solve():
    # U(t=0, x) = 0
    U_old.fill(0)

    row = 2
    maximum = 0

    while maximum > eps and row < stop_iteration:
        for i in range(1, N - 1):
            U_new[i] = 0.5 * (U_old[i + 1] + U_old[i - 1]) - 0.5 * dt / dx * (
                    (U_old[i + 1] * U_old[i + 1]) / 2 - (U_old[i - 1] * U_old[i - 1]) / 2
            )

        # U(t, x=0) = 1
        # U(t, x=1) = 0
        U_new[0], U_new[-1] = 1, 0

        maximum = find_absolute_max()

        U_old[:] = U_new
        row += 1

    return row

elapsed_time = timeit.timeit(solve, number=1)
print(f"calculating time: {elapsed_time:.6f} seconds")
print("Number of iterations:", solve())

# Plotting
plt.plot(x, U_new)
plt.xlabel("x")
plt.ylabel("U")
plt.legend()
plt.show()
