#Approach One 
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

#Approach Two
from collections import Counter

def appear_once(array):
    count = Counter(array)
    for element, freq in count.items():
        if freq == 1:
            return element
        
#Approach Three
def appears_once(array):
    count = {}
    for element in array:
        if element in count:
            count[element] += 1 
        else:
            count[element] = 1 
    
    # Count of elements that appeared once
    u = 0 
    for i, j in count.items():
        if j == 1:
            u += 1
            print('Unique element:', i)
    print('Number of unique elements is', u)


array = [1,2,3,1,2,3,5]

print(appears_once(array)) # 5