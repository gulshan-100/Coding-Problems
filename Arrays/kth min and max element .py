def kth_min_max(arr,k):
    arr.sort()
    kth_min_max_elements = {"min": arr[k-1], "max": arr[-k]}
    return kth_min_max_elements

arr = [23,1,2,5,87,4]
k = 2
result = kth_min_max(arr,k)
print(k, "th min and max elements are: ", result['min'], result['max'])
