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
                high = mid - 1
        return False
    
    def searchMatrix(matrix, target):
        # iterate this row
        for i in range(len(matrix)):
            # print(matrix[i][0]) # first number on row
            if target < matrix[i][0]:
                Solution.binarySearch(matrix[i-1], target)
            elif target == matrix[i][0]:
                return True
            else:
                if Solution.binarySearch(matrix[i], target):
                    return True
        
        return False
                
            
    


# print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 15))
# print(Solution.searchMatrix([[1]], 1))
print(Solution.searchMatrix([[1, 3]], 3))