import numpy as np

def to_check(m):
    for i in m:
        if i > 0:
            return True
    return False

def simplex_method():
    constr = 2
    var = 2

    matrix = []
    for i in range(constr):
        row = list(map(float, input(f"Coeffs for constr {i+1}: ").split()))
        matrix.append(row)
    matrix = np.array(matrix)
    obj_f = list(map(float, input("Coeffs for the obj func: ").split()))
    obj_f2 = obj_f.copy() 
    z = np.zeros(constr)
    z2 = np.zeros(var + constr)
    #позволяет увеличить значение целевой функции при движении к оптимуму
    while to_check(obj_f):
        piv_col_idx = np.argmax(obj_f)
        print('piv_col_idx : ',  piv_col_idx)
        piv_col = matrix[:, piv_col_idx]
        print("piv_col:  ", piv_col)
        min_pos_val = float('inf')
        piv_row_idx = -1
        for i in range(len(matrix)):
            element = matrix[i][-1] / piv_col[i] 
            if piv_col[i] > 0 and element < min_pos_val: 
                #выбор 0 or negative будет уводить нас из области, вне которой решений не существует
                min_pos_val = element
                piv_row_idx = i
                print("piv_row_idx: " , piv_row_idx)
        matrix[piv_row_idx] /= piv_col[piv_row_idx]
        print("matrix[piv_row_idx]: " , matrix[piv_row_idx])
        z[piv_row_idx] = obj_f2[piv_col_idx]

        for i in range(len(matrix)):
            if i != piv_row_idx:
                m2 = matrix[i][piv_col_idx] #множитель m2, который представляет собой значение из опорного столбца для данной строки
                if m2 != 0:
                    matrix[i] -= matrix[piv_row_idx] * m2   #Новая строка = Новая строка – Коэффициент строки в ведущем столбце * Новая Ведущая строка

        for i in range(len(obj_f)):
            n = np.dot(matrix[:, i], z)
            z2[i] = n

        for i in range(len(obj_f)):
            obj_f[i] = obj_f2[i] - z2[i]

    x = matrix[0][-1]
    y = matrix[1][-1]
    first_element = obj_f2[0]
    second_element = obj_f2[1]
    maximum = first_element * x + second_element * y  

    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Maximum: {maximum}")

simplex_method()




"""import numpy as np

def to_check(m):
    for i in m:
        if i > 0:
            return True
    return False

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

    while to_check(obj_function):
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

if __name__ == "__main__":
    simplex_method()
"""



"""import numpy as np

def positive_value(arr):
    for val in arr:
        if val > 0:
            return True
    return False

def simplex_method():
    const = 2
    var = 2

    matrix = np.array([[1, 1, 1, 0, 2], [2, 1, 0, 1, 2]], dtype=float)
    objective_function = [-7, -6, 0, 0]  
    objective_function_2 = [-7, -6, 0, 0]
    z_values = np.zeros(const)
    zero_arr = np.zeros(var + const)

    while positive_value(objective_function):
        pivot_col_idx = np.argmax(objective_function)
        pivot_col = matrix[:, pivot_col_idx]

        min_pos_el = float('inf')
        pivot_row_idx = -1
        for i in range(len(matrix)):
            min_el = matrix[i][-1] / pivot_col[i]
            if pivot_col[i] > 0 and min_el < min_pos_el:
                min_pos_el = min_el
                pivot_row_idx = i

        matrix[pivot_row_idx] /= pivot_col[pivot_row_idx]
        z_values[pivot_row_idx] = objective_function_2[pivot_col_idx]

        for i in range(len(matrix)):
            if i != pivot_row_idx:
                multiplier = matrix[i][pivot_col_idx]
                if multiplier != 0:
                    matrix[i] -= matrix[pivot_row_idx] * multiplier

        for i in range(len(objective_function)):
            dot_product = np.dot(matrix[:, i], z_values)
            zero_arr[i] = dot_product

        for i in range(len(objective_function)):
            objective_function[i] = objective_function_2[i] - zero_arr[i]

    x1_val = matrix[0][-1]
    x2_val = matrix[1][-1]
    max_val = -(objective_function[0] * x1_val + objective_function[1] * x2_val)

    print(f"x1 = {x1_val}")
    print(f"x2 = {x2_val}")
    print(f"Maximum: {max_val}")

simplex_method()"""

"""
import numpy as np

def checking(m):
    for i in m:
        if i > 0:
            return True
    return False

def simplex_method():
    number_of_constraints = 2
    number_of_variables = 2

    matrix = np.array([[1, 1, 1, 0, 4], [2, 1, 0, 1, 6]], dtype=float) #?
    obj_function = [-7, -6, 0, 0]  
    obj_func2 = [-7, -6, 0, 0]
    z = np.zeros(number_of_constraints)
    zero2 = np.zeros(number_of_variables + number_of_constraints)

    while checking(obj_function):
        pivot_col_index = np.argmax(obj_function)
        pivot_col = matrix[:, pivot_col_index]

        min_pos_el = float('inf')
        pivot_row_index = -1
        for i in range(len(matrix)):
            min_el = matrix[i][-1] / pivot_col[i]
            if pivot_col[i] > 0 and min_el < min_pos_el:
                min_pos_el = min_el
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
    maximum = -(obj_function[0] * x + obj_function[1] * y)

    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Maximum: {maximum}")
simplex_method()"""


"""import numpy as np

def has_positive_value(arr):
    for val in arr:
        if val > 0:
            return True
    return False

def simplex_method():
    const = 3
    var = 2

    matrix = np.array([[1, 1, 1, 0], [2, 1, 0, 1]], dtype=float)
    objective_function = [-7, -6, 0, 0]
    objective_function_2 = [-7, -6, 0, 0]
    z_values = np.zeros(const)
    zero_arr = np.zeros(var + const)

    rhs_values = np.array([4, 6]) #right-hand side values

    while has_positive_value(objective_function):
        pivot_col_idx = np.argmax(objective_function)
        pivot_col = matrix[:, pivot_col_idx]

        min_pos_el = float('inf')
        pivot_row_idx = -1
        for i in range(len(matrix)):
            if pivot_col[i] > 0:
                quotient = rhs_values[i] / pivot_col[i]
                if quotient < min_pos_el:
                    min_pos_el = quotient
                    pivot_row_idx = i

        matrix[pivot_row_idx] /= pivot_col[pivot_row_idx]
        z_values[pivot_row_idx] = objective_function_2[pivot_col_idx]

        for i in range(len(matrix)):
            if i != pivot_row_idx:
                multiplier = matrix[i][pivot_col_idx]
                if multiplier != 0:
                    matrix[i] -= matrix[pivot_row_idx] * multiplier

        for i in range(len(objective_function)):
            dot_product = np.dot(matrix[:, i], z_values)
            zero_arr[i] = dot_product

        for i in range(len(objective_function)):
            objective_function[i] = objective_function_2[i] - zero_arr[i]

    x1_val = matrix[0][-1]
    x2_val = matrix[1][-1]
    max_val = -(objective_function[0] * x1_val + objective_function[1] * x2_val)

    print(f"x1 = {x1_val}")
    print(f"x2 = {x2_val}")
    print(f"Maximum: {max_val}")

simplex_method()
"""

"""import numpy as np

def checking(m):
    for i in m:
        if i > 0:
            return True
    return False
def Simplex_method():
    number_of_constraints ,number_of_variables  = 2 , 2
    matrix = np.array([[ 1 , 1 , 1 , 0 , 4] , [2 , 1 , 0 , 1 ,6]], dtype=float)
    obj_function = np.array([-7 , -6 , 0 ,0])
    obj_func2 = np.array([-7 , -6 , 0 ,0]) 
    z = np.zeros(number_of_constraints) 
    zero2 = np.zeros(number_of_variables + number_of_constraints) 
    while checking(obj_function):
        pivot_col_index = int(np.where(obj_function == max(obj_function))[0])
        print(' pivot_col_index : ',  pivot_col_index)
        pivot_col = matrix[:, pivot_col_index:pivot_col_index + 1]
        print("pivot col:  " , pivot_col)
        pivot_col = pivot_col.flatten()
        quotient_var = matrix[:, -1]
        exact_quotient = np.divide(quotient_var, pivot_col)
        pivot_row_index = int(np.where(exact_quotient == min(exact_quotient))[0])
        print("pivot_row_index: " , pivot_row_index)
        matrix[pivot_row_index] = matrix[pivot_row_index] / matrix[pivot_row_index, pivot_col_index]
        print("matrix[pivot_row_index]: " , matrix[pivot_row_index])
        z[pivot_row_index] = obj_func2[pivot_col_index]
        for i in range(len(matrix)):
            if i != pivot_row_index:
                mul = matrix[i, pivot_col_index]
                print(mul)
                if mul != 0:
                    matrix[i] = matrix[i] - matrix[pivot_row_index] * mul
            print(matrix[i])
        print()
        for i in range(len(matrix[0, :-1])):
            n = np.dot(matrix[:, i], z)
            zero2[i] = n
        print("zero2: " , zero2)
        obj_function =  obj_func2 - zero2
        print("Objective function: " , obj_function)
    print("maximum: ", np.dot(z, quotient_var))
print(Simplex_method())
"""

"""import numpy as np

def simplex_method():
    constr = 2
    var = 2

    matrix = []
    for i in range(constr):
        row = list(map(float, input(f"Coeffs for constr {i+1}: ").split()))
        matrix.append(row)
    matrix = np.array(matrix)
    obj_f = list(map(float, input("Coeffs for the obj func: ").split()))
    obj_f2 = obj_f.copy() 
    z = np.zeros(constr)
    z2 = np.zeros(var + constr)

    while True:
        piv_col_idx = np.argmin(obj_f)
        print(' piv_col_idx : ',  piv_col_idx)
        piv_col = matrix[:, piv_col_idx]
        print("piv_col:  ", piv_col)
        min_pos_val = float('inf')
        piv_row_idx = -1
        for i in range(len(matrix)):
            element = matrix[i][-1] / piv_col[i]
            if piv_col[i] > 0 and element < min_pos_val:
                min_pos_val = element
                piv_row_idx = i
                print("piv_row_idx: " , piv_row_idx)
        matrix[piv_row_idx] /= piv_col[piv_row_idx]
        print("matrix[piv_row_idx]: " , matrix[piv_row_idx])
        z[piv_row_idx] = obj_f2[piv_col_idx]

        for i in range(len(matrix)):
            if i != piv_row_idx:
                m2 = matrix[i][piv_col_idx]
                if m2 != 0:
                    matrix[i] -= matrix[piv_row_idx] * m2

        for i in range(len(obj_f)):
            n = np.dot(matrix[:, i], z)
            z2[i] = n

        for i in range(len(obj_f)):
            obj_f[i] = obj_f2[i] - z2[i]

    x = matrix[0][-1]
    y = matrix[1][-1]
    first_element = obj_f2[0]
    second_element = obj_f2[1]
    maximum = first_element * x + second_element * y  

    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Maximum: {maximum}")


simplex_method()"""