# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> str:
        result = []
        n = len(chars)
        lp = 0
        for i in range(n-1):
            rp = chars[i]
            print(chars[lp], rp)
            
        
    
chars = ["a","a","b","b","c","c","c"]
# chars = ["a"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
solution = Solution()
solution.compress(chars)