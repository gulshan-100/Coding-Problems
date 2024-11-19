def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    return count       

string = "Gulshan"
print(count_vowels(string)) # 2