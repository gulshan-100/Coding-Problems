def union(a, b):
    return list(set(a) | set(b))

def intersection(a,b):
    return list(set(a) & set(b))

a1 = [1,2,3,4,5,6,7]
a2 = [4,5,6,7,8,9,10]

print("Union : ", union(a1, a2))
print("Intersection : ", intersection(a1, a2))
