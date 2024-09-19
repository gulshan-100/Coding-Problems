# Python code to merge dict using update() method
def Merge(dict1, dict2):
    return(dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

#1st method: Using update() method
print(dict1 | dict2 )

#2nd method:
print(Merge(dict1, dict2))