def remove_duplicates(array):
    s = set()
    result = []
    for element in array:
        if element not in s:
            s.add(element)
            result.append(element)
    return result
    
array = [1, 3, 4,6,6,6,7, 2, 2]
print(remove_duplicates(array))
print(type(remove_duplicates(array))) 