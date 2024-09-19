def appraoch_one(arr, element):
    return element in arr

def approach_two(arr, element):
    for i in range(0, len(arr)):
        if arr[i] == element:
            return True
    return False

arr = [1,2,3,4,5]
element = 7
print(appraoch_one(arr, element))
