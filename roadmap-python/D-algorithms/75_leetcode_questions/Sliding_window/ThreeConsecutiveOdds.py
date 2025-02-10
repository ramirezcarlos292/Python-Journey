def threeConsecutiveOdds(arr):
    n = len(arr)
    k = 3
    if n < k:
        return False

    for i in range(n):
        window = arr[i:i+k]
        if len(window) == k:
            print(window)
            print(window[0]%2, window[1]%2, window[2]%2)
            if (window[0]%2) and (window[1]%2) and (window[2]%2) == 1:
                return True
            flag = False
    
    return flag
    
# print(threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
# print(threeConsecutiveOdds([2,6,4,1]))
print(threeConsecutiveOdds([1,1,1]))