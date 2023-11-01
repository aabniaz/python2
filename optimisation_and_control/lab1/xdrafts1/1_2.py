import numpy as np
import matplotlib.pyplot as plt

c = [-7, -6]
A = [
    [1, 1],
    [2, 1]
]
b = [4, 6]

c.extend([0] * (len(b) + 1))

for i in range(len(A)):
    A[i].extend([0] * len(A))

for i in range(len(A)):
    A[i][-len(A) + i] = 1

for i in range(len(b)):
    A[i].append(b[i])

A.append(c)

def Simplex(A):

    def find_pivot_column(c):
        pivot_col = np.argmin(c)
        if all(row[pivot_col] <= 0 for row in A):
            return None

        return pivot_col

    def find_pivot_row(pivot_col):
        ratios = []

        for i in range(len(A)):
            if A[i][pivot_col] > 0:
                ratios.append((i, A[i][-1] / A[i][pivot_col]))
        pivot_row = min(ratios, key=lambda x: x[1])[0]
        return pivot_row

    pivot_col = find_pivot_column(c)
    pivot_row = find_pivot_row(pivot_col)

    pivot_element = A[pivot_row][pivot_col]
    for j in range(len(A[0])):
        A[pivot_row][j] /= pivot_element

    for i in range(len(A)):
        if i != pivot_row:
            factor = A[i][pivot_col]
            for j in range(len(A[0])):
                A[i][j] -= factor * A[pivot_row][j]

Simplex(A)

x_values = np.linspace(0, 10, 400)  
y_values = np.minimum(4 - x_values, 6 - 2 * x_values)

def plot_feasible_solution(c, A, x_values, y_values, maximum):
    plt.figure()
    plt.plot(x_values, (maximum - c[0] * x_values) / c[1], label='Objective Function: 7x + 6y')
    plt.plot(x_values, 4 - x_values, label='Constraint 1: x + y = 4')
    plt.plot(x_values, 6 - 2 * x_values, label='Constraint 2: 2x + y = 6')

    plt.fill_between(x_values, y_values, where=(y_values >= 0), interpolate=True, alpha=0.2, color='gray', label='Feasible Region')

    # Add feasible solution points
    x_feasible = np.array([2.0])
    y_feasible = np.array([2.0])
    plt.scatter(x_feasible, y_feasible, color='red', label='Feasible Solution Points')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.axvline(x=0, color='k', linestyle='--')
    plt.axhline(y=0, color='k', linestyle='--')
    plt.title('Feasible Region and Objective Function')
    plt.legend()
    plt.grid()
    plt.show()

plot_feasible_solution(c, A, x_values, y_values, A[-1][-1])
