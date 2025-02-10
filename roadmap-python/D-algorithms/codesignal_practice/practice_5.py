def solution(input_string):
    # TODO: Implement the function to check whether the provided string is a palindrome or not.
    filtered = ''.join([c.lower() for c in input_string if c.isalnum()])
    lp = 0
    rp = len(filtered)-1
    
    while lp < rp:
        print(filtered[lp], filtered[rp])
        if filtered[lp] != filtered[rp]:
            # print(filtered[lp], filtered[rp])
            return False
        lp += 1
        rp -= 1
    
    return True
    
if __name__ == "__main__":
    print(solution("level"))
    print(solution("Level"))
    print(solution("Sofia"))
    print(solution("L!evel!"))
    print(solution("race a car"))