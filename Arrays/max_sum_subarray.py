def max_sum_subarray(array):
    max_sum = current_sum = array[0]
    for element in array[1:]:
        current_sum = max(element, current_sum + element)
        max_sum = max(max_sum, current_sum)
    return  max_sum
        
array = [1,-1,3,4,-2,1]

print(max_sum_subarray(array))