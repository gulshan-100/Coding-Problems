def missing_number(array):
    n = max(array)
    s = n * (n+1) // 2
    result = s - sum(array)
    return result
        
array = [3, 0, 1,2,5]
print(missing_number(array)) # 2
