from icecream import ic
def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        ic(left_arr)
        right_arr = arr[len(arr)//2:]
        ic(right_arr)

        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0 #left array idx
        j = 0 #right array idx
        k = 0 #merge array idx

#compare numbers in arrays
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1   


arr_test = [2,3,4,5,1,7,4,4,4,8,5]
merge_sort(arr_test)
print(arr_test)