# import string
# print(string.ascii_letters)
def solution(s):
    ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers_list = "0123456789"
    ### if not in ascii letters or numbers_list means is symbol
    
    next_letter = ""
    result = ""
    for i in range(len(s)):
        char_s = s[i]
        if char_s in ascii_letters:
            # print(char_s)
            for k in range(len(ascii_letters)):
                if char_s == ascii_letters[k]:
                    if char_s == "Z":
                        next_letter = "A"
                    elif char_s == "z":
                        next_letter = "a"
                    else:
                        next_letter = ascii_letters[k+1]
            # result.append(next_letter)
            result += "".join(next_letter)
        elif char_s in numbers_list:
            # result.append(char_s)
            result += "".join(char_s)
        else:
            result += "".join(char_s)
    print(result)          
    # return result  
                    
    # prev_letter = "x"
    # for k in range(len(ascii_letters)):
    #     if prev_letter == ascii_letters[k]:
    #         # next_letter = "A" if prev_letter == "Z" else (ascii_letters[k+1]) # position k+1, will return next letter in list
    #         if prev_letter == "Z":
    #             next_letter = "A"
    #         elif prev_letter == "z":
    #             next_letter = "a"
    #         else:
    #             next_letter = ascii_letters[k+1]
    # print(next_letter)
    
solution("abc123XYz!")

