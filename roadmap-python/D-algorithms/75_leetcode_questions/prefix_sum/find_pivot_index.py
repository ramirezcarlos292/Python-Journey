class Solution:
    def pivotIndex(nums) -> int:
        pivot = 1
        nums = [0] + nums + [0]
        
        for i in range(1, len(nums)-1):
            leftSum = sum(nums[:i])
            rightSum = sum(nums[i+1:])
            if (rightSum == leftSum) and (leftSum != 0) and (rightSum != 0):
                return nums[i]
            if (rightSum == 0) and (leftSum == 0):
                return 0
        return -1
            
            
    def pivotIndexNC(nums):
        total = sum(nums)
        
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        
        return -1
    
print(Solution.pivotIndexNC([1,7,3,6,5,6]))
print(Solution.pivotIndexNC([1,2,3]))
print(Solution.pivotIndexNC([2, 1, -1]))
print(Solution.pivotIndexNC([-1, 1, 2]))