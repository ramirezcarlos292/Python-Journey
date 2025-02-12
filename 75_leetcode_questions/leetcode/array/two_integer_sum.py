class Solution:
    def twoSum(nums, target):
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
                
        
Solution.twoSum([3,4,5,6], 7)
Solution.twoSum([4,5,6], 10)
Solution.twoSum([5,5], 10)