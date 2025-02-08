def isPalindrome(x):
    A = str(x)
    B = A[::-1]
    print(A)
    print(B)
    if A==B:
        return 'true'
    else:
        return 'false'

print(isPalindrome(10))
