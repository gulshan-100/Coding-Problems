from collections import Counter

def check_anagram(string1, string2):
    if len(string1) != len(string2):
        return False 
    
    return Counter(string1) == Counter(string2)

def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

string1 = "listen"
string2 = "silent"

print(check_anagram(string1, string2))