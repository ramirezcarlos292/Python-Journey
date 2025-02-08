def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return abs(x * y) // gcd(x, y)

# Example usage
num1 = 12
num2 = 18
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")