class Solution:
    def makeFancyString(s):
        result = []
        result.append(s[0])
        counter = 0
        for i in range(1, len(s)):
            if result[-1] != s[i]:
                result.append(s[i])
                counter = 0
            elif result[-1] == s[i] and counter < 1:
                result.append(s[i])
                counter += 1

        return "".join(result)
        
        
print(Solution.makeFancyString("leeetcode"))