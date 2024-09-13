def check_rotations(string1, string2):
    if len(string1) != len(string2):
        return False 
    
    temp_str = string1 + string1 
    
    return string2 in temp_str 

string1 = "Hello"
string2 = "elloH"

print(check_rotations(string1, string2)) 