class Solution:
    def reverseVowels(s: str) -> str:
        l = len(s)
        output = [""] * l
        
        vowels = ["a","e","i","o","u"]
        vowels_letters = []
        vowels_loc = []
        for i in range(l):
            letter = s[i]
            if letter.lower() in vowels:
                # vowel_in_s[i] = letter
                vowels_letters.append(letter)
                vowels_loc.append(i)
            else:
                output[i] = letter
        
        reversed_vowels = vowels_letters[::-1]
        
        for k in range((len(reversed_vowels)-1), -1, -1):
            output[vowels_loc[k]] = reversed_vowels[k]
            
        output = "".join(output)

        return output
        
        
Solution.reverseVowels("IcecreAm")