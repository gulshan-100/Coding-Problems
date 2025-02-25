def consecutive_senquence(array):
    nums = set(array) 
    result = []
    for element in nums:
        if element - 1 not in nums:
            count = 0 
            while (element + count) in nums:
                count += 1 
                result.append(count)
    return max(result) if result else 0
            

array = [100, 4, 200, 1, 3, 2,5]
print(consecutive_senquence(array))