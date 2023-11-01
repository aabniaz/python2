import numpy as np

def to_check(m):
    for i in m:
        if i < 0:
            return True
    return False

def simplex_method():
    constr = 2
    var = 2

    matrix = np.array(np.array([[ 1 , 1 , 1 , 0 , 4] , [2, 1 , 0 , 1 ,6]], dtype=float))
    obj_f = np.array([-7 , -6 , 0 ,0])
    obj_f2 = obj_f.copy() 
    z = np.zeros(constr)
    z2 = np.zeros(var + constr)
    #позволяет увеличить значение целевой функции при движении к оптимуму
    while to_check(obj_f):
        piv_col_idx = np.argmin(obj_f)
        print('piv_col_idx: ', piv_col_idx)
        piv_col_elem = matrix[:, piv_col_idx]
        print('piv_col_elem:  ', piv_col_elem)
        min_pos_val = float('inf')
        piv_row_idx = -1

        for i in range(len(matrix)):
            element = matrix[i][-1] / piv_col_elem[i] 
            if piv_col_elem[i] > 0 and element < min_pos_val: 
                #выбор 0 or negative будет уводить нас из области, вне которой решений не существует
                min_pos_val = element
                piv_row_idx = i
        
        print("piv_row_idx: " , piv_row_idx)
        matrix[piv_row_idx] /= piv_col_elem[piv_row_idx]
        print("matrix[piv_row_idx]: ", matrix[piv_row_idx])
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
    maximum = -(first_element * x + second_element * y)  

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