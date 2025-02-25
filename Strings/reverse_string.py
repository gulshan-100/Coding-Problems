def reverse_string(string):
    return string[::-1]

#another approach 
def reverse_string_2(string):
    str_list = list(string)
    start = 0
    end = len(string) - 1 
    while (start < end):
        str_list[start], str_list[end] = str_list[end], str_list[start]
        start += 1
        end -= 1
    result = "".join(str_list)
    return result        
        
string = "Gulshan"
print(reverse_string_2(string))