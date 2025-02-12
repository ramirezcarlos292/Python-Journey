## not optimized
import math
def productExceptSelf(nums):
    answer = []
    for i in range(len(nums)):
        product = 1
        # get other items except i
        sides =  nums[:i] + nums[i+1:]
        # find their product
        product = math.prod(sides)
        # append its final result to answer
        answer.append(product)
        
    return answer
     
print(productExceptSelf([1, 2, 3, 4]))

print(productExceptSelf([-1, 1, 0, -3, 3]))
