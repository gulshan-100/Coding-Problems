#For one point rotation 
def rotate(arr):
    n = len(arr)
    last_element = arr[-1]
    
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
        
    arr[0] = last_element
    return arr

#For multiple point rotation
def rotate2(arr, k):
    if not arr:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k]



arr = [1,2,3,4,5]
print(arr)
print(rotate(arr))
print(rotate2(arr, 2))