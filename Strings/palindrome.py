def check_palindrome(string):
    return string == string[::-1]

string = "abba"
string2 = "Gulshan"

print(check_palindrome(string))
print(check_palindrome(string2))