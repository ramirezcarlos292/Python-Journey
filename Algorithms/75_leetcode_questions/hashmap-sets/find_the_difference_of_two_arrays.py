class Solution:
    def findDifference(nums1, nums2):
        result = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        arr0 = list(nums1-nums2)
        arr1 = list(nums2-nums1)
        
        result.append(arr0)
        result.append(arr1)
        
        return result
        
print(Solution.findDifference([1,2,3], [2,4,6]))