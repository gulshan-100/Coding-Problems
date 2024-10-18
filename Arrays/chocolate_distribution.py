def chocolate_distribution(arr, m):
    n = len(arr)
    arr.sort()
    
    minDiff = float('inf')
    
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < minDiff:
            minDiff = diff
        
    return minDiff

arr = [7, 3, 2, 4, 9, 12, 56]
m = 3

print(chocolate_distribution(arr, m))   