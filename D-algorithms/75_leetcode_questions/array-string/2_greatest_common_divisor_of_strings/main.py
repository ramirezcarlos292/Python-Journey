# 1071. Greatest Common Divisor of Strings
def gcdOfStrings1(str1: str, str2: str) -> str:
    len1, len2 = len(str1), len(str2)

    greater = len1 if len1 > len2 else len2
    
    while True:
        if (greater % len1 == 0) and (greater % len2 == 0):
            lcm = greater
            break
        greater += 1
    
    gcd = int((len1 * len2) / lcm)

    str_gcd1 = str1[:gcd]*(int(len2/gcd))    
    str_gcd2 = str2[:gcd]*(int(len1/gcd))

    if ((str_gcd1 == str2) & (str_gcd2 == str1)):
        return(str1[:gcd])
    else:
        return("")

def gcdOfStrings2(self, str1: str, str2: str) -> str:
    if str1+str2 != str2+str1:
        return ""
    
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    gcd_length = gcd(len(str1), len(str2))
    return str1[:gcd_length]
    
# print(gcdOfStrings1("ABCABC", "ABC"))
# print(gcdOfStrings1("ABABAB", "ABAB"))
# print(gcdOfStrings1("LEET", "CODE"))

print(gcdOfStrings2("ABCABC", "ABC"))
print(gcdOfStrings2("ABABAB", "ABAB"))
print(gcdOfStrings2("LEET", "CODE"))