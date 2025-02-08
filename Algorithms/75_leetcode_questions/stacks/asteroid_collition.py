class Solution:
    def asteroidsCollision(asteroids):
        stack = []
        
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                # incoming asteroid was negative and won
                if diff < 0:
                    stack.pop()
                # incoming asteroid was negative and lose
                elif diff > 0:
                    a = 0
                # incoming asteroid and prev asteroid are equal in mass
                # both will be destroyed
                else:
                    a = 0
                    stack.pop()
            # If incoming asteroid survived all while loops, append it
            if a:
                stack.append(a)
                    
        return stack         
                    
         
# Solution.asteroidsCollision([8,-8])
print(Solution.asteroidsCollision([5,10,-5]))
# print(Solution.asteroidsCollision([10,2,-5]))


        