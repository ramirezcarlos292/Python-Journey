class Solution:
    def isSubsequence2(s: str, t: str) -> bool:
        i, j = 0, 0
        while i <len(s) and j <len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            j+=1
        return True if i == len(s) else False
        
print(Solution.isSubsequence2("abc", "ahbgdc"))
print(Solution.isSubsequence2("axc", "ahbgdc"))
print(Solution.isSubsequence2("ab", "baab"))
print(Solution.isSubsequence2("", "ahbgdc"))
print(Solution.isSubsequence2("b", "abc"))
