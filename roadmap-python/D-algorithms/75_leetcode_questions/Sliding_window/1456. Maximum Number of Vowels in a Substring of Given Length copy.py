def maxVowels(s, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    l = len(s)
    max_v_count = 0
    for i in range(l-k+1):
        v_count = 0
        win_s = list(s[i:i+k])
        for j in range(k):
            if (win_s[j] in vowels):
                v_count += 1
        
                
        max_v_count = max(max_v_count, v_count)


    return max_v_count

# output = 3
s = "abciiidef"
k = 3

# # output = 2
# s = "aeiou"
# k = 2

# output = 2
# s = "leetcode"
# k = 3

print(maxVowels(s, k))