def remove_consecutive_characters(string):
    result = ""
    last_element = None 
    
    for element in string:
        if element != last_element:
            result += element 
            last_element = element
            
    return result

string = "aabbcc"
string2 = "abc"
print(remove_consecutive_characters(string)) # abc
print(remove_consecutive_characters(string2)) # abc