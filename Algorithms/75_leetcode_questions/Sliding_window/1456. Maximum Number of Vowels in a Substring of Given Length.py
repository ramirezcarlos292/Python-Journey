def maxVowels(s, k):
    vowel = {'a','e','i','o','u'}

    l, cnt, res = 0, 0, 0
    for r in range(len(s)):
        cnt += 1 if s[r] in vowel else 0
        if r - l + 1 > k:
            cnt -= 1 if s[l] in vowel else 0
            l += 1
        res = max(res, cnt)

    return res    
            
    
# output = 3
s = "abciiidef"
k = 3

# # output = 2
# s = "aeiou"
# k = 2

# # output = 2
# s = "leetcode"
# k = 3

print(maxVowels(s, k))