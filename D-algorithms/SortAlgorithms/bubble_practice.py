class Solution:
    def bubbleSort(arr):
        length = len(arr)
        
        for i in range(length):
            swapped = False
            
            for j in range(0, length-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            
            if swapped == False:
                break
            
        return arr 
    
if __name__ == "__main__":
    arr = Solution.bubbleSort([5,4,9,7,3,6,99,78,8,0,94,7,4,9,10])
    print(arr)