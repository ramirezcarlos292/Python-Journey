class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        total_letters = word1 + word2
        word1 = list(word1)
        word2 = list(word2)
        final_string = ''
        for idx, item in enumerate(total_letters):
            if idx<len(word1):
                final_string = final_string+word1[idx]
            if idx<len(word2):
                final_string = final_string+word2[idx]
        return final_string


print(Solution.mergeAlternately("abc", "pqr")
print(Solution.mergeAlternately("ab", "pqrs")
print(Solution.mergeAlternately("abcd", "pq")