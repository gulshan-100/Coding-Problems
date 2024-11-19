def count_characters(string):
    count = {}
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count       

string = "Gulshan"
print(count_characters(string)) # {'G': 1, 'u': 1, 'l': 1, 's': 1, 'h': 1, 'a': 1, 'n': 1}