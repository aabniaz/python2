"""import numpy as np
import matplotlib.pyplot as plt

def checking(m):
    for i in m:
        if i > 0:
            return True
    return False

def plot_feasible_solution(matrix, x_values, y_values, maximum):
    plt.figure()
    plt.plot(x_values, y_values, label='Feasible Region')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axvline(x=0, color='k', linestyle='--')
    plt.axhline(y=0, color='k', linestyle='--')
    plt.scatter(matrix[:, 0], matrix[:, 1], color='red', label='Optimal Solution (x, y)')
    plt.title(f'Feasible Region and Optimal Solution\nMaximum Value: {maximum}')
    plt.legend()
    plt.grid()
    plt.show()

def simplex_method():
    number_of_constraints = 2
    number_of_variables = 2

    matrix = []
    for i in range(number_of_constraints):
        row = list(map(float, input(f"Enter coefficients for constraint {i+1} (separated by space): ").split()))
        matrix.append(row)
    matrix = np.array(matrix)

    obj_function = list(map(float, input("Enter coefficients for the objective function (separated by space): ").split()))

    obj_func2 = obj_function.copy()

    z = np.zeros(number_of_constraints)
    zero2 = np.zeros(number_of_variables + number_of_constraints)

    while checking(obj_function):
        pivot_col_index = np.argmax(obj_function)
        pivot_col = matrix[:, pivot_col_index]

        min_quotient = float('inf')
        pivot_row_index = -1
        for i in range(len(matrix)):
            quotient = matrix[i][-1] / pivot_col[i]
            if pivot_col[i] > 0 and quotient < min_quotient:
                min_quotient = quotient
                pivot_row_index = i

        matrix[pivot_row_index] /= pivot_col[pivot_row_index]
        z[pivot_row_index] = obj_func2[pivot_col_index]

        for i in range(len(matrix)):
            if i != pivot_row_index:
                mul = matrix[i][pivot_col_index]
                if mul != 0:
                    matrix[i] -= matrix[pivot_row_index] * mul

        for i in range(len(obj_function)):
            n = np.dot(matrix[:, i], z)
            zero2[i] = n

        for i in range(len(obj_function)):
            obj_function[i] = obj_func2[i] - zero2[i]

    x = matrix[0][-1]
    y = matrix[1][-1]
    first_element = obj_func2[0]
    second_element = obj_func2[1]
    maximum = first_element * x + second_element * y

    print("Calculated values:")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Maximum: {maximum}")

    # Prepare data for plotting feasible region
    x_values = np.linspace(0, max(x, y) + 1, 400)
    y_values = (obj_func2[1] - obj_func2[0] * x_values) / obj_func2[1]

    # Plot the feasible region and optimal solution
    plot_feasible_solution(matrix, x_values, y_values, maximum)

if __name__ == "__main__":
    simplex_method()
"""

import numpy as np
import matplotlib.pyplot as plt

def checking(m):
    for i in m:
        if i > 0:
            return True
    return False

def plot_feasible_solution(matrix, obj_function, x_values, y_values, maximum):
    plt.figure()
    plt.plot(x_values, (maximum - obj_function[0] * x_values) / obj_function[1], label='Objective Function: 7x + 6y = 26')
    plt.plot(x_values, (matrix[0, 2] - matrix[0, 0] * x_values) / matrix[0, 1], label='Constraint 1: x + y ≤ 4')
    plt.plot(x_values, (matrix[1, 2] - matrix[1, 0] * x_values) / matrix[1, 1], label='Constraint 2: 2x + y ≤ 6')

    plt.fill_between(x_values, y_values, where=(y_values >= 0) & (y_values <= 6 - 2*x_values), interpolate=True, alpha=0.2, color='gray', label='Feasible Region')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.axvline(x=0, color='k', linestyle='--')
    plt.axhline(y=0, color='k', linestyle='--')
    plt.scatter(matrix[:, 0], matrix[:, 1], color='red', label='Optimal Solution (x, y)')
    plt.title(f'Feasible Region and Optimal Solution\nMaximum Value: {maximum}')
    plt.legend()
    plt.grid()
    plt.show()

def simplex_method():
    number_of_constraints = 2
    number_of_variables = 2

    matrix = []
    for i in range(number_of_constraints):
        row = list(map(float, input(f"Enter coefficients for constraint {i+1} (separated by space): ").split()))
        matrix.append(row)
    matrix = np.array(matrix)

    obj_function = list(map(float, input("Enter coefficients for the objective function (separated by space): ").split()))

    obj_func2 = obj_function.copy()

    z = np.zeros(number_of_constraints)
    zero2 = np.zeros(number_of_variables + number_of_constraints)

    while checking(obj_function):
        pivot_col_index = np.argmax(obj_function)
        pivot_col = matrix[:, pivot_col_index]

        min_quotient = float('inf')
        pivot_row_index = -1
        for i in range(len(matrix)):
            quotient = matrix[i][-1] / pivot_col[i]
            if pivot_col[i] > 0 and quotient < min_quotient:
                min_quotient = quotient
                pivot_row_index = i

        matrix[pivot_row_index] /= pivot_col[pivot_row_index]
        z[pivot_row_index] = obj_func2[pivot_col_index]

        for i in range(len(matrix)):
            if i != pivot_row_index:
                mul = matrix[i][pivot_col_index]
                if mul != 0:
                    matrix[i] -= matrix[pivot_row_index] * mul

        for i in range(len(obj_function)):
            n = np.dot(matrix[:, i], z)
            zero2[i] = n

        for i in range(len(obj_function)):
            obj_function[i] = obj_func2[i] - zero2[i]

    x = matrix[0][-1]
    y = matrix[1][-1]
    first_element = obj_func2[0]
    second_element = obj_func2[1]
    maximum = first_element * x + second_element * y

    print("Calculated values:")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Maximum: {maximum}")

    # Prepare data for plotting feasible region
    x_values = np.linspace(0, max(x, y) + 1, 400)
    y_values = np.minimum((maximum - obj_function[0] * x_values) / obj_function[1],
                          (matrix[0, 2] - matrix[0, 0] * x_values) / matrix[0, 1],
                          (matrix[1, 2] - matrix[1, 0] * x_values) / matrix[1, 1])

    # Plot the feasible region and optimal solution
    plot_feasible_solution(matrix, obj_function, x_values, y_values, maximum)

if __name__ == "__main__":
    simplex_method()
