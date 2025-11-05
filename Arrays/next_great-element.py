def finding_NGE(array):
    result = []
    for i in range(len(array)):
        next_greater = -1
        for j in range(i+1, len(array)):
            if array[j] > array[i]:
                next_greater = array[j]
                break
        result.append(next_greater)
    return result

arr = [4, 5, 2, 25]
print(finding_NGE(arr))  # Output: [5, 25, 25, -1]
