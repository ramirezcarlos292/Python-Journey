# 1768. Merge Strings Alternately
# O(n^2) approach
def mergeAlternately(word1: str, word2: str) -> str:
    total_letters = word1 + word2
    word1 = list(word1)
    word2 = list(word2)
    final_string = ''
    for idx, item in enumerate(total_letters):
        if idx < len(word1):
            final_string += word1[idx]
        if idx < len(word2):
            final_string += word2[idx]
    return final_string

'''
Better because once one of the words ends it stops the loop and just append what is left of each word.
Appending then joining is preferable.
'''
def mergeAlternately2(word1: str, word2: str) -> str:
    i, j = 0, 0
    res = []
    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j])
        i += 1
        j += 1
    res.append(word1[i:])
    res.append(word2[j:])
    
    return "".join(res)            

print(mergeAlternately("abc", "pqr"))
print(mergeAlternately("ab", "pqrs"))
print(mergeAlternately("abcd", "pq"))

print(mergeAlternately2("abc", "pqr"))
print(mergeAlternately2("ab", "pqrs"))
print(mergeAlternately2("abcd", "pq"))