import re
class Solution:
    def palindrome(string: str) -> bool:
        string = string.lower().replace(" ", "")
        l = 0
        r = len(string) - 1
        
        while l <= r:
            if string[l] != string[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    
    def palindrome2(string: str) -> bool:
        string = string.lower().replace(" ", "")
        print(string)
        return string == string[::-1]

print(Solution.palindrome('Anita lava la tina'))
print(Solution.palindrome2('Anita lava la tina'))