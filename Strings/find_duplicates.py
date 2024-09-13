from collections import Counter

def find_duplicates(string):
    char_count = Counter(string)
    
    duplicates = [char for char, count in char_count.items() if count > 1]
    
    return duplicates
    
        
        
string = "GulshanG"

print(find_duplicates(string))