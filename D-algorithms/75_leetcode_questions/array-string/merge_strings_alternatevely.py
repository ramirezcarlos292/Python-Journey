def mergeAlternatevly(word1, word2):
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
        
# word1 = "abc"
# word2 = "pqr" 
# word1 = "ab"
# word2 = "pqrs"
word1 = "abcd"
word2 = "pq"
print(mergeAlternatevly(word1, word2))
