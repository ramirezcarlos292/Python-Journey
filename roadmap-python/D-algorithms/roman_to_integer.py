def romanToInt(s):
    dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    S = list(s)
    

    # def minus_numbers(S):
    #     for i in range(len(S)):
    #         if S[i] == 'I':
    #             if (S[i+1] == "V") or (S[i+1] == "X"):
    #                 return -1
    #         if S[i] == 'X':
    #             if (S[i+1] == "L") or (S[i+1] == "C"):
    #                 return -10
    #         if S[i] == 'C':
    #             if (S[i+1] == "D") or (S[i+1] == "M"):
    #                 return -100

    def minus_numbers(S, i):
        if len(S) == 2:
            if S[i] == 'I':
                if (S[i+1] == "V") or (S[i+1] == "X"):
                    return -1
                else:
                    return 1
            if S[i] == 'X':
                if (S[i+1] == "L") or (S[i+1] == "C"):
                    return -10
                else:
                    return 10
            if S[i] == 'C':
                if (S[i+1] == "D") or (S[i+1] == "M"):
                    return -100
                else:
                    return 100
            else:
                return dic[S[i]]
        else:
            return dic[S[i]]
    
    rti = 0
    elements = []
    # print(S)
    for idx, item in enumerate(S):
        # question if item will be negative or not
        # print(idx)
        print(minus_numbers(item, idx))                                                                                                                
    
romanToInt("IV")
# romanToInt("VI")
# romanToInt("IX")
# romanToInt("XI")
# romanToInt("III")
# romanToInt("LVIII")
# romanToInt("MCMXCIV")