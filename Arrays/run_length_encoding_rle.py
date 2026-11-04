def result(data) : 
    result = []
    count = 1 
    for i in range(len(data)-1) : 
        if data[i] == data[i + 1] : 
            count += 1 
        else : 
            result.append(data[i] + str(count)) 
            count = 1
    result.append(data[-1] + str(count))
    result = ''.join(result)
    return result

data = "aaaaabbbbcccdde"
print(result(data))