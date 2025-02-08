def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

print(is_palindrome("racecar"))  # Output: True
