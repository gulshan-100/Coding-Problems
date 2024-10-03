def two_sum(array, target):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return [array[i], array[j]]
            
array = [1, 2, 3, 4, 5]
target = 9

print(two_sum(array, target)) # [3, 4]