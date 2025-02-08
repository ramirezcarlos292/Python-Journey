class MySolution:
    def gcdOfStrings(str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

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
            print(str1[:gcd])
        else:
            print("")

class ProSolution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1+str2 != str2+str1:
            return ""
        
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]
    
MySolution.gcdOfStrings("ABCABC", "ABC")
MySolution.gcdOfStrings("ABABAB", "ABAB")
MySolution.gcdOfStrings("LEET", "CODE")