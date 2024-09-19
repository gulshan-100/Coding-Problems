def count_ones(array):
    count = 0
    maximum = 0
    for i in range(0, len(array)):
        if array[i] == 1:
            count += 1
        else:
            count = 0
        maximum = max(count, maximum)
    return maximum

array = [1,1,1,0,1,1,1,1,1]

print(count_ones(array)) # 5