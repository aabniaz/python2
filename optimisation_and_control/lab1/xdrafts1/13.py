# second [[1,2,0,1,0,0,1200],[0,2,1,0,1,0,1800],[4,0,1,0,0,1,3600],[1,6,8,0,0,0]]  maximize
# first   [[4,1,1,1,0,0,1800],[2,2,1,0,1,0,2000],[4,2,1,0,0,1,3200] , [6,8,5,0,0,0]]  maximize
# third [[ 1 , 2  1 , 0 , 12] , [1 , 1 , 0 , 1 ,10] , [6 , 8 , 0 ,0]] minimize
import numpy as np
a = input("""You want to solve problem with Simplex method ? Yes or No
Your choice: """)
def checking(m):
    for i in m:
        if i < 0:
            return True
    return False
def Simplex_method():
    number_of_constraints ,number_of_variables  = 2 , 2
    matrix = np.array([[ 1 , 2 , 1 , 0 , 12] , [1 , 1 , 0 , 1 ,10]], dtype=float)
    obj_function = np.array([6 , 8 , 0 ,0])
    obj_func2 = np.array([6 , 8 , 0 ,0]) 
    z = np.zeros(number_of_constraints) 
    zero2 = np.zeros(number_of_variables + number_of_constraints) 
    while checking(obj_function):
        pivot_col_index = int(np.where(obj_function == max(obj_function))[0])
        #print(' pivot_col_index : ',  pivot_col_index)
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
if a == "Yes" :
    print(Simplex_method())