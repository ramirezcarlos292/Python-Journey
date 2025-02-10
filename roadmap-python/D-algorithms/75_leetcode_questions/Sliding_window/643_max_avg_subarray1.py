def findMaxAve(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(len(nums) - k):
        window_sum = window_sum - nums[i] + nums[i + k]
        
        max_sum = max(max_sum, window_sum)
    
    return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAve(nums, k))