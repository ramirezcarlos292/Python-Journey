def inv(s):
    if len(s) % 2:
        for item in range(len(s)-1):
            print(item)
    else:
        return "odd"

# for item in range(len(text)):



print(inv("hello"))
print(inv("abcdef"))