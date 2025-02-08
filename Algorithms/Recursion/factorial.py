def factorial(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)

print(factorial(6))  # Output: 720 (6! = 1 * 2 * 3 * 4 * 5 * 6)
