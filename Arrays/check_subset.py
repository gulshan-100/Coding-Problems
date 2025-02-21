from collections import Counter

def approach_one(a1, a2): 
    count_a1 = Counter(a1)
    count_a2 = Counter(a2)
    
    for element in a2:
        if count_a2[element] > count_a1[element]:
            return False                
    return True

def approach_two(a1, a2):
    temp_list = a1 
    for element in a2:
        if element in temp_list:
            temp_list.remove(element)
        else:
            return False
    return True       

def approach_three(a1,a2):
    s1 = set(a1)
    s2 = set(a2)
    return s2.issubset(s1)  

a1 = [1,2,3,4,5]
a2 = [1,2,3]
a3 = [1,2,3,6]

print(approach_one(a1,a2))
print(approach_one(a1,a3))

    