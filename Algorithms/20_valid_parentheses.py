class Solution:
    def isValid(s):
        if len(s) < 2:
            return False
        map = {
            ')':'(',
            '}':'{',
            ']':'[',
            # '(':')',
            # '{':'}',
            # '[':']'
        }
        op = ['(','[','{']
        cl = [')',']','}']

        stk = []
        for p in s:
            if p in op:
                stk.append(p)
            elif p in cl:
                if len(stk) == 0:
                    return False
                elif map[p] == stk[-1]:
                    stk.pop()
                else:
                    return False
        return True
    



class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        map = {')':'(', '}':'{', ']':'['}
        stk = []

        for p in s:
            if p in map:
                if stk and stk[-1] == map[p]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(p)
        return True if not stk else False
    
    
print(Solution.isValid("([])"))