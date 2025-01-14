def kmost_frequency(array, k):
    counts = {}
    for element in array:
        if element in counts:
            counts[element] += 1 
        else:
            counts[element] = 1 
    # Sort elements by frequency
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    n = 0 
    result = []
    for element, count in sorted_counts:
        if n < k:
            result.append(element)
            n += 1  # Increment n for each added element
    return result 

array = [354,3543,34,324,1,1,1,1,34,45,45,45,45,45,45,45,45]
k = 2
print(kmost_frequency(array, k))
