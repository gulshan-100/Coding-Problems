list1 = [1,3,5]
list2 = [2,4,6]

merged_list = []
i = j = 0 

def merged_lists(list1, list2):
    global i, j
    while (i < len(list1)) and (j < len(list2)):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    return merged_list

print(merged_lists(list1, list2))