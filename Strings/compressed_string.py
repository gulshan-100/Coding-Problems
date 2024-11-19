def compressed_string(string):
    if not string:
        return ""
    
    compressed = []
    count = 1
    
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            compressed.append(string[i-1] + str(count))
    
    compressed.append(string[-1]+str(count))
    
    compressed = "".join(compressed)
    
    return compressed 

string  ='aaabbccdaa'
print(compressed_string(string)) # ['a3', 'b2', 'c2', 'd1', 'a2']