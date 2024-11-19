#Approach One - TC : 0(n), SC : 0(1)
def check_sorting(array):
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            return False 
    return True 

#Approach Two - TC : 0(1), SC : 0(1)
def check_array_sort(array):
    return array == sorted(array)