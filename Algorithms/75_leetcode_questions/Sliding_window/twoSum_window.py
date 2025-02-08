def twoSum(nums, target):
    for i in range(len(nums)):  
        if (len(nums[i:i+2])==2) and (nums[i] + nums[i+1] == target):
            return [i, i+1]


nums = [2,7,11,15]
target = 9

# nums = [3,2,4] 
# target = 6

# nums = [3,3]
# target = 6

# nums = [3,2,3]
# target = 6

print(twoSum(nums, target))