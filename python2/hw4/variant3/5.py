def monotonicity(arr):
    changes = [i for i in range(len(arr) - 1) if arr[i] != arr[i + 1]]
    return changes
    
print(monotonicity([0, 1]))      
print(monotonicity([0, 2, 1]))   
print(monotonicity([0, 1, 1, 0])) 
