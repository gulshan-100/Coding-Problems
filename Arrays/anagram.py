from collections import Counter

def check_anagram(s, t):
    first_str = Counter(s) 
    second_str = Counter(t)
    return first_str == second_str

#another approach 
def check_anagram(s, t):
    return sorted(s) == sorted(t)

#another approach
def check_anagram(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] not in t:
            return False
    return True

#another approach
def check_anagram_dict(s,t):
    first_count = {}
    second_count = {}
    for element in s:
        if element in first_count:
            first_count[element] += 1
        else:
            first_count[element] = 1
    for element in t:
        if element in second_count:
            second_count[element] += 1
        else:
            second_count[element] = 1
    return first_count == second_count


a = 'gulshan'
b = 'ulshang'
print(check_anagram(a, b))
    
      