import numpy as np
import matplotlib.pyplot as plt

start_x, end_x = 0, 1
dx, dt = 0.001, 0.001
eps = 1e-6
u = 1
N = int((end_x - start_x)/dx + 1)
stop_iteration = int(1e6)
x = np.linspace(start_x, end_x, N)
U, U_new = np.zeros(N), np.zeros(N)
def abs_max():
    return np.max(np.abs(U_new - U))
row = 2
maximum = 0
while True:
    for i in range(1, N - 1):
        U_new[i] = 0.5 * (U[i + 1] + U[i - 1]) - 0.5 * dt / dx * (
                (U[i + 1] * U[i + 1]) / 2 - (U[i - 1] * U[i - 1]) / 2
        )
    # U(t, x=0) = 1
    # U(t, x=1) = 0
    U_new[0], U_new[-1] = 1, 0
    maximum = abs_max()
    U[:] = U_new
    row += 1
    if not (maximum > eps and row < stop_iteration):
        break
#print("Number of iterations:", row)
plt.plot(x, U_new)
plt.xlabel("x")
plt.ylabel("U")
plt.show()