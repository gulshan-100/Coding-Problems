def count_consonents(string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char not in vowels and char.isalpha())
    return count

string = "Gulshan"
print(count_consonents(string)) # 5