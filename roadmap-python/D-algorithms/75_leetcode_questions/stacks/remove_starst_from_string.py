def viz_stack(stack):
    for item in range(len(stack)-1,-1,-1):
        print(stack[item])

result = []   
def removeStars(s: str) -> str:
    stack = []
    result = []
    count = 0
    # put all chars in string into a stack
    for item in s:
        print(stack)
        stack.append(item)
    
    for item in range(len(stack)):
        print(stack)
        stack.pop()

            
## Comments section - Stacks are implemented in python as arrays
# stack =[]
# it's methods are:
# ADD TO TOP: an item into the stack stack.append(value)
# REMOVE FROM TOP: what is in top of the stack is stack.pop()
# PEEK: stack[-1]
    
## evaluate     
removeStars("leet**cod*e") # expected = "lecoe"
# Solution.removeStars("erase*****") # expected = "lecoe"