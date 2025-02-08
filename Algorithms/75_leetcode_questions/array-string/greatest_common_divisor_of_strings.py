def gcdOfStrings(str1, str2):
    l_str1 = list(str1)
    l_str2 = list(str2)
    gcd = ""
    counter = 0
    prev_pfix = 0
    if len(str1) <= len(str2):
        mystr = str1
    else:
        mystr = str2

    while counter < len(mystr):
        gcd += mystr[counter]
        pfix_curr = mystr.count(gcd)
        if pfix_curr >= prev_pfix:
            prev_pfix = pfix_curr
            pfix = gcd
        
        counter+=1
    print(prev_pfix, pfix)

    
    
    
    

str1 = "ABCABC"
str2 = "ABC"
# str1 = "ABABAB"
# str2 = "ABAB"
# str1 = "LEET"
# str2 = "CODE"

gcdOfStrings(str1, str2)


    # while counter < len(l_str1):
    #     gcd += l_str1[counter]
    #     pfix_curr = str1.count(gcd)
    #     if pfix_curr >= prev_pfix:
    #         prev_pfix = pfix_curr
    #         pfix = gcd
        
    #     counter+=1
    # print(prev_pfix, pfix)