def max_and_min(arr):
    arr.sort()
    minmax = {"min":arr[0], "max":arr[-1]}
    return minmax

def approach_two(array):
    max = array[0]
    for i in range(1, len(array)):
        if (array[i]> max):
            max = array[i]
    return max

def minimum(array):
    minimum = float('inf')
    for element in array:
        if element < minimum:
            minimum = element
    return minimum

def maximum(array):
    maximum = float('-inf')
    for element in array:
        if element > maximum:
            maximum = element
    return maximum

arr = [23,34,2,53,25]
result = max_and_min(arr)
print("Minimum element : ", result["min"])
print("Maximum element : ", result['max'])
