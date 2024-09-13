def sort_zeros_ones_twos(arr):
    c0 = 0
    c1 = 0
    c2 = 0
    
    for num in arr:
        if num == 0:
            c0 += 1
        elif num == 1:
            c1 += 1
        else:
            c2 += 1

    idx = 0
    
    for i in range(c0):
        arr[idx] = 0
        idx += 1
    
    for i in range(c1):
        arr[idx] = 1
        idx += 1
        
    for i in range(c2):
        arr[idx] = 2
        idx += 1

arr = [1,1,2,0,2,1,0,2,1,0,0,1]
print(arr)
result = sort_zeros_ones_twos(arr)
print(arr)