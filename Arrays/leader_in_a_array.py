def find_leaders(array):
    n = len(array)
    leaders = []
    max_so_far = array[-1]
    leaders.append(max_so_far)
    
    for i in range(n-2, -1,-1):
        if array[i] > max_so_far:
            leaders.append(array[i])
            max_so_far = array[i]
    return leaders[::-1]            
                
array = [10,34,5,7,4]

print(find_leaders(array)) # [34, 7, 4]