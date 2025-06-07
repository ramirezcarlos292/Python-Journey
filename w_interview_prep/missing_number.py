# approach: sort the input arr, use two pointers, left l, right r, calculate the diff
# between r - l if diff is equal to 2, return r-1 or  return l + 1, and terminate the process
# if r exhaust the length of array return r + 1 to be the missing number.


def missingNumber(arr):
    # sort [1, 2, 4, 5]
    arr.sort(reverse=False)
    l = 0
    r = 1
    end = len(arr)
    while r < end:
         if arr[r]-arr[l] == 2:
             return arr[r] - 1
         l += 1
         r += 1
    return arr[l] + 1
# inputs
# input1 = [3, 0, 1]
# input2 = [4, 5, 6, 3, 2, 0]
print(missingNumber([5, 2, 4, 1]))
print(missingNumber([4, 5, 6, 3, 2, 0]))
print(missingNumber([0, 1, 2, 3, 4]))