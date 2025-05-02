class Solution:
    def binarySearch(row, target):
        low = 0
        high = len(row) - 1
        
        while low <= high:
            mid = low + (high - low) //2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid -1
            
        return False

        
        
    
    def searchMatrix(nums, target):
        # iterate this row
        for i in range(1, len(nums)):
            # print(nums[i][0]) # first number on row
            if target < nums[i][0]:
                if Solution.binarySearch(nums[i-1], target):
                    return True
        
        return False
                
            
    


print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))