import heapq
def heapsort(arr):
    heapq.heapify(arr) # convert array into a heap
    n = len(arr)
    new_list = [0] * n # create an array to store sorted items
    for i in range(n):
        minn = heapq.heappop(arr) # pop minimum of heap
        new_list[i] = minn  # append minimum to new list
    return new_list # sorted array

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
