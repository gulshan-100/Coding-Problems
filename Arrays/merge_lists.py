#approach one 
def approach_one(list1, list2):
    return list1 + list2

def approach_two(list1, list2):
    list1.extend(list2)
    return list1

def approach_three(list1, list2):
    for item in list2:
        list1.append(item)
    return list1

