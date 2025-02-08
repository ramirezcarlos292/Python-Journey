class Solution:
    def asteroidsCollision(asteroids):
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                temp = stack[-1]
                # diff = a + stack[-1]
                diff = a + temp
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
            
        return stack
           




# print(Solution.asteroidsCollision([8,-8]))
# print(Solution.asteroidsCollision([5,10,-5]))
print(Solution.asteroidsCollision([10,2,-5]))