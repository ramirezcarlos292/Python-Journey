'''
    Divide and conquer algorithm.

    The key process in quickSort is a partition() . The target of partitions is to place the pivot  
    and put all smaller elements to the left of the pivot, and all greater elements to the right of the pivot.
    
    choice of pivot
    Pick the first element as a pivot .
    Pick the last element as a pivot.
    Pick a random element as a pivot .
    Pick the middle as the pivot.
    
    Time Complexity:
        Average Case: O(N * logN), where N is the length of the array.
        Best Case: O(N * logN)
        Worst Case: O(N2)
    Space Complexity: O(1)
'''

from icecream import ic

# Pick the middle as the pivot.
def quick_sort(arr):
    # if array have 1 or less than one element, return array since it is already sorted
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1] # arr[len(arr) // 2] # arr[0], if first element wanted to be picked, arr[-1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # recursive method
    return quick_sort(left) + middle + quick_sort(right)


# Example usage:
data = [1,5,6,3,9,8]
sorted_data = quick_sort(data)
print("Sorted Array in Ascending Order:")
print(sorted_data)


