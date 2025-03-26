class Solution:
    def productExceptSelf(nums):
        p = [1] * (len(nums))
        p[0] = nums[0]
        # prefix
        for i in range(1, len(nums)):
            p[i] = p[i - 1] * nums[i]
        print(p)
        
        # sufix
        s = [1] * (len(nums))
        s[0] = nums[-1]
        for i in range(len(nums)-1,0,-1):
            s[i] = p[i - i] * nums[i]
        print(s)
        
                
        
        

nums = [1,2,3,4]
# Output: [24,12,8,6]
print(Solution.productExceptSelf(nums))

nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
print(Solution.productExceptSelf(nums))