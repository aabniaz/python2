#код не универсальный
import numpy as np

def checking(obj_function):
    for i in obj_function:
        if i > 0:
            return True
    return False

def simplex_method(number_of_constraints, number_of_variables, constraint_coefficients, objective_coefficients):
    matrix = np.array(constraint_coefficients)
    obj_function = np.array(objective_coefficients)
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
    maximum = np.dot(obj_func2, [x, y])

    print("Calculated values:")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Maximum: {maximum}")

if __name__ == "__main__":
    number_of_constraints = int(input("Enter the number of constraints: "))
    number_of_variables = int(input("Enter the number of variables: "))

    constraint_coefficients = []
    for i in range(number_of_constraints):
        row = list(map(float, input(f"Enter coefficients for constraint {i+1} (separated by space): ").split()))
        constraint_coefficients.append(row)

    objective_coefficients = list(map(float, input("Enter coefficients for the objective function (separated by space): ").split()))

    simplex_method(number_of_constraints, number_of_variables, constraint_coefficients, objective_coefficients)
""