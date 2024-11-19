def remove_whitespaces(string):
    
    #approach one 
    string = "".join(string.split())
    
    #approach two
    string2 = string.replace(" ", "")
    
    #approach three 
    string3 = "".join([char for char in string if char != " "])
    
    return string3

string = "Gulshan Kumar"
print(remove_whitespaces(string)) # GulshanKumar