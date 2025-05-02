def removeStars(s: str) -> str:
    stack = []
    stack2 = []
    result = ""
    # push items in s inversely
    for item in range(len(s)-1,-1,-1):
        stack.append(s[item])  
    
    while (stack):
        # peek item
        item = stack[-1]
        if item == "*":
            stack.pop()
            stack2.pop()
        else:
            out = stack.pop()
            stack2.append(out)      
    
    return "".join(stack2)
    
print(removeStars("leet**cod*e")) # expected = "lecoe"
print(removeStars("erase*****"))
