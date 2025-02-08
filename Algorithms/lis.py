def lis(arr):
    l = len(arr)

    if l <= 1:
        return l
    result = 1
    lp = arr[0]
    
    for n in range(1, l):
        rp = arr[n]
        if rp >= lp:
            result += 1
            lp = rp
        
            
    return result


print(lis([10, 22, 9, 33, 21, 50, 41, 60, 80]))
print(lis([1]))
print(lis([1,2,3,4,5,6,3,8]))
print(lis([7,6,5,4,3,2,1]))