class Solution(object):
    def isBalanced(self, num):
        even_product = 1
        odd_product = 1 

        for i in range(len(num)):
            digit = int(num[i])  # Convert the character to an integer
            if i % 2 == 0:
                even_product += digit   
            else:
                odd_product += digit
    
        return even_product == odd_product
    
#Approach two
def check_balance(string):
    even = 0
    odd = 0
    
    for i in range(0, len(string), 2):
        even += int(string[i])
    
    for j in range(1, len(string), 2):
        odd += int(string[j])
    
    return even == odd

# Example usage:
solution = Solution()
print(solution.isBalanced("123456"))  # Output: True
print(solution.isBalanced("12345"))   # Output: False
