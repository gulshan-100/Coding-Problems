import numpy as np 

def search_matrix(array, target):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == target:
                return True    
    return

array = np.array([[1,3,5,7],[10,11,16,20],[23,30,34,60]])
target = 500

print(search_matrix(array, target)) # True

