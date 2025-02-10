def reverseWords(s):
    arry = s.split(" ")
    l = len(arry)
    output = []
    for item in range(l, 0, -1):
        if (arry[item - 1] != ""):
            output.append(arry[item - 1])
    output = " ".join(output)
    return output
    
print(reverseWords("the sky is blue"))
print(reverseWords("hello world"))
print(reverseWords("a good   example"))