def rearrange(arr):
    positives = []
    negatives = []
    
    for element in arr:
        if element < 0:
            negatives.append(element)
        else:
            positives.append(element)
        
    return negatives + positives
    
def rearrange2(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

arr = [2,4,-4,2,-5]
rearrange2(arr)
print(arr)



