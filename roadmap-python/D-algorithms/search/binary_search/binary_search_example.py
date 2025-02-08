class Solution:
    def bin_search(arr, target):
        # 0 index position
        low = 0
        high = len(arr)-1
        
        while low <= high:
            # get the middle of array
            mid = low + (high - low) // 2
            # check if target is at mid
            if arr[mid] == target:
                return mid
            # if target is greater, ignore left half
            elif arr[mid] < target:
                low = mid + 1
            # if target is smaller, ignore right half
            else:
                high = mid - 1
        
        # element not found
        return -1
    
    
            
        
        
print(Solution.bin_search([2,5,8,12,16,23,38,56,72,91], 56))
print(Solution.bin_search([2,5,8,12,16,23,38,56,72,91], 8))