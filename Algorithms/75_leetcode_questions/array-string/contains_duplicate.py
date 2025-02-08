def containsDuplicate(nums):
    map = {}
    for idx, item in enumerate(nums):
        #is incoming item already in dict_values
        #if yes, return true
        if item in map:
            return True
        #if not, add to dict_values
        map[item] = idx
    return False
    
    # if no items already in dict_values
    # return false
            


# cases
nums = [1,2,3,1]
nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicate(nums))