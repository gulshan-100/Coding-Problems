def largest_next_number(array):
    result = []
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[j] > array[i]:
                result.append(array[j])
                break
    return result

arr = [2, 7, 3, 5, 4, 6, 8]
print(largest_next_number(arr))  