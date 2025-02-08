# Explanation of Heaps
# https://www.youtube.com/watch?v=E2v9hBgG6gE&ab_channel=GregHogg

# MIN HEAPS
# Building a heap using heapify, Time: O(n), Space: O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9] 

import heapq
heapq.heapify(A)
print(A)

# OPERATIONS ON HEAPS
# HEAP PUSH (Insert element) Time: O(log n)
heapq.heappush(A, 4)
print(A)

# HEAP POP (Extract minimum element) Time: O(log n)
minn = heapq.heappop(A)
print(A, minn)

# HEAPSORT USING MAX_HEAP
# Time: O(n log n), Space: O(n), Space: O(1)  is possible via swapping, but requires extra steps
def heapsort(arr):
    heapq.heapify(arr) # convert array into a heap
    n = len(arr)
    new_list = [0] * n # create an array to store sorted items
    for i in range(n):
        minn = heapq.heappop(arr) # pop minimum of heap
        new_list[i] = minn  # append minimum to new list
    return new_list # sorted array

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# HEAP PUSH POP Time: O(log n)
heapq.heappushpop(A, 99)
print(A)

# PEEK MINIMUM item in heap: Time: O(1)
print(A[0])

# BUILD HEAP FROM SCRATCH (item by item) Time: O (n log n)
# heapify would do this in O(n), but sometimes this might be useful
B = [-5,4,2,1,7,0,3] 
heap = []

for x in B:
    heapq.heappush(heap, x) # push each incoming item in the for loop into the heap
    print(heap, len(heap)) # check size of heap

### MIN HEAP
C = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9] 
n = len(C)

for i in range(n):
    C[i] = -C[i] # convert to its negative, so when is sorted smaller number will be minimum

heapq.heapify(C)
print(C)

largest = - heapq.heappop(C) # Then minus sign here will convert it to be the maximum of heap
print(largest)

heapq.heappush(C, -7) # Inserts positive 7 into the heap, 7 would add -7 
print(C)

    
# PRIORITY QUEUES USING HEAPS 
# hash map, counting elements in heap
D = [5,4,3,5,4,3,5,5,4]

from collections import Counter
counter = Counter(D) # Count how many of each item is in the list D and map this into a dictionary
print(counter)

# Then we can push into the heap each pair value, key, where value will be the priority is given to each key
heap = []
for key, value in counter.items():
    # print(key, value)
    heapq.heappush(heap, (value, key))
print(heap)