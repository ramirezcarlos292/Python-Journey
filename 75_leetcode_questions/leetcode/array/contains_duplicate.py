class Solution:
    def hasDuplicate(words):
        firstRow = set("qwertyuiop")
        secondRow = set("asdfghjkl")
        thirdRow = set("zxcvbnm")
        result = []
        
        for word in words:
            word_set = word.lower()
            word_set = set(word_set)
            if len(word_set-firstRow) == 0 or len(word_set-secondRow) == 0 or len(word_set-thirdRow) == 0:
                result.append(word)
        
        return result
        
                
                
s = "racecar"
t = "carrace"

print(Solution.hasDuplicate(["Hello","Alaska","Dad","Peace"]))
print(Solution.hasDuplicate(["omk"]))
print(Solution.hasDuplicate(["adsdf","sfd"]))

