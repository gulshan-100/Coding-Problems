from copy import copy, deepcopy

# Original list
a = [[1, 2, 3], [4, 5, 6]]

# --- Shallow Copy ---
b = copy(a)
b[0][0] = 10

print("After modifying b (shallow copy):")
print("a:", a)   # a is affected because inner lists are shared
print("b:", b)
print("---")

# --- Deep Copy ---
c = deepcopy(a)
c[0][0] = 20

print("After modifying c (deep copy):")
print("a:", a)   # a is NOT affected
print("c:", c)
