def two_sum(array, target):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return [array[i], array[j]]
            
array = [1, 2, 3, 4, 5]
target = 9

def two_sum2(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

# Example usage:
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]

    

print(two_sum2(array, target)) # [3, 4]