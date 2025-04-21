def zeroes_at_the_end(array):
    non_zero_index = 0 
    for element in array:
        if element !=0:
            array[non_zero_index] = element
            non_zero_index += 1
    for i in range(non_zero_index, len(array)):
        array[i] = 0
    return array

array = [0, 1, 0, 3, 12,0,0,3,4,5,3,0,0,6]
print(zeroes_at_the_end(array)) # [1, 3, 12, 0, 0]