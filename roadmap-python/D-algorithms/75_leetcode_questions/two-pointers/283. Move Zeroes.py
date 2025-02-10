def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            print(nums[l])
            print(nums[r])
            l+=1
    return nums

nums = [0,1,0,3,12]
# nums = [1,0,1]

print(moveZeroes(nums))