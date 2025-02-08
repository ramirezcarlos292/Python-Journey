class Solution:
    def maxArea(height) -> int:
        lp = height[0]
        counter = 1
        accum = []
        for i in range(1, len(height)):
            rp = height[i]
            accum.append(rp*counter)
        return accum
            
            
                
        
        # return area
        
print(Solution.maxArea([1,8,6,2,5,4,8,3,7]))
# print(Solution.maxArea([1,1]))
# print(Solution.maxArea([0,1]))
# print(Solution.maxArea([0,0,1]))
# print(Solution.maxArea([1,2,1]))