def remove_element(arr, element):
    for ele in arr:
        if ele == arr[element]:
            arr.remove(ele)
    return arr

def remove_element2(arr, element):
    result = [x for x in arr if x != element]
    return result
    
arr = [1,2,3,4,5]
element = 3
print(remove_element2(arr, element))