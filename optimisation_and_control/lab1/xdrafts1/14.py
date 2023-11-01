import numpy as np

def to_check(m):
    for i in m:
        if i < 0:
            return True
    return False

def create_matrix():
    num_constraints = int(input("Enter the number of constraints: "))
    num_variables = int(input("Enter the number of variables: "))
    matrix = []
    print("Enter the coefficients for each constraint in the format 'a1 a2 ... an b':")
    for i in range(num_constraints):
        row = list(map(float, input(f"Coefficients for constraint {i+1}: ").split()))
        matrix.append(row)

    # Adding the slack variables and the objective function coefficients
    for i in range(num_constraints):
        matrix[i].extend([0] * i + [1] + [0] * (num_constraints - i - 1))
    
    matrix = np.array(matrix, dtype=float)
    return matrix

def create_obj_function():
    print("Enter the coefficients for the objective function:")
    obj_f = list(map(float, input("Coefficients: ").split()))
    
    return np.array(obj_f, dtype=float)

def simplex_method(matrix, obj_f):
    constr = 2
    var = 2

    """matrix = np.array(np.array([[ 1 , 1 , 1 , 0 , 4] , [2, 1 , 0 , 1 ,6]], dtype=float))
    obj_f = np.array([-7 , -6 , 0 ,0])"""
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


    print("Placeholder: Rest of the simplex method code goes here.")
matrix = create_matrix()
obj_f = create_obj_function()
# Create the matrix and objective function


# Call the simplex method
simplex_method(matrix, obj_f)
