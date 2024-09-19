def appears_once(array):
    for i in range(len(array)):
        element = array[i]
        
        count = 0
        
        for j in range(len(array)):
            if array[j] == element:
                count += 1
            
        if count == 1:
            return element
    return None

array = [1,2,3,1,2,3,5]

print(appears_once(array)) # 5