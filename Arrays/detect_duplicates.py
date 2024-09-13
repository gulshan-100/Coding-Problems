def duplicates(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
            
def duplicates2(arr):
 def findDuplicate(self, nums):
    tortoise = nums[0]
    rare = nums[0]
        
    #phase 1
    while True:
        tortoise = nums[tortoise]
        rare = nums[nums[rare]]
        if tortoise == rare:
            break 
    #phase2 
    tortoise = nums[0]
    while tortoise != rare:
        tortoise = nums[tortoise]
        rare = nums[rare]
            
    return rare
       
arr = [1, 3, 4, 2, 2] 
print(duplicates2(arr))   