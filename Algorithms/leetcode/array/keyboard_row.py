class Solution:
    def findWords(words):
        firstRow = "qwertyuiop"
        secondRow = "asdfghjkl"
        thirdRow = "zxcvbnm"
        result = []
              
        for word in words:
            tmp1, tmp2, tmp3 = "", "", ""
            for letter in word:
                if (letter.lower() in firstRow):
                    tmp1 += letter
                elif (letter.lower() in secondRow):
                    tmp2 += letter
                elif (letter.lower() in thirdRow):
                    tmp3 += letter
                else:
                    tmp1, tmp2, tmp3 = "", "", ""
                    break
            if len(tmp1) == len(word) or len(tmp2) == len(word) or len(tmp3) == len(word):
                result.append(word)

        return result




Solution.findWords(["Hello","Alaska","Dad","Peace"])
Solution.findWords(["omk"])
Solution.findWords(["adsdf","sfd"])