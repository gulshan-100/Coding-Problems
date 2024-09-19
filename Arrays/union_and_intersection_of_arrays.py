def union(a, b):
    return list(set(a) | set(b))

def intersection(a,b):
    return list(set(a) & set(b))

def find_union(array1, array2):
    s = set()
    union = []
    
    for element in array1:
        s.add(element)
        
    for element in array2:
        s.add(element)
        
    for number in s:
        union.append(number)
        
    return union

a1 = [1,2,3,4,5,6,7]
a2 = [4,5,6,7,8,9,10]

print("Union : ", union(a1, a2))
print("Intersection : ", intersection(a1, a2))
