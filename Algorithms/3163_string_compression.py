class Solution:
    def compressedString(word):
        letter = word[0]
        next_letter = word[0]
        accum = 0
        result = ""
        for i in range(1, len(word)):
            if letter == word[i] and accum < 9:
                accum += 1
            else:
                result += (str(accum) + letter)
                accum = 1
                letter = word[i]

        return result
    

print(Solution.compressedString("abcde"))
print(Solution.compressedString("aaaaaaaaaaaaaabb"))