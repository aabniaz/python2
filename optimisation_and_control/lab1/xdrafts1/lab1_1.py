import numpy as np

def get_input_matrix():
    # Take input for constraint matrix
    constr = int(input("Enter the number of constraints: "))
    var = int(input("Enter the number of variables: "))

    matrix = np.zeros((constr, var + 1))

    print("Enter the constraint matrix (one row at a time, separating elements with spaces):")
    for i in range(constr):
        matrix[i] = list(map(float, input().split()))

    return matrix, constr, var

def get_input_objective(var):
    # Take input for objective function coefficients
    print("Enter the coefficients for the objective function (separated by spaces):")
    obj_f = np.array(list(map(float, input().split())))
    obj_f2 = obj_f.copy()

    # Pad with zeros if the number of coefficients doesn't match the number of variables
    if len(obj_f) < var:
        obj_f = np.pad(obj_f, (0, var - len(obj_f)), 'constant')

    return obj_f, obj_f2
    
def to_check(m):
    for i in m:
        if i < 0:
            return True
    return False

def simplex_method():
    matrix, constr, var = get_input_matrix()
    obj_f, obj_f2 = get_input_objective(var)

    z = np.zeros(constr)
    z2 = np.zeros(var + constr)

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

