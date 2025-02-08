## Traverse an array in reverse
arr = [1, 2, 3, 4, 5]
for i in range(len(arr)-1, -1, -1):
    print(i)
    
    
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[::-1]

arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)  # Output: [5, 4, 3, 2, 1]