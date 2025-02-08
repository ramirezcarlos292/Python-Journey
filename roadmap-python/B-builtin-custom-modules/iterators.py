# https://www.geeksforgeeks.org/iterators-in-python/
# 
# Example 1: Intro to Iterators
# s = "GFG"
# it = iter(s)

# print(next(it))
# print(next(it))
# print(next(it))
# if overboard, throws an error
# print(next(it))

# Example 2: Custom Iterator
# class EvenNumbers:
#     def __iter__(self):
#         self.n = 2 # start from first even number
#         return self
    
#     def __next__(self):
#         x = self.n
#         self.n += 2 # increment by two every time it runs
#         return x
    
# even = EvenNumbers()
# # it refer to iteration
# it = iter(even)

# run_times = 8 # # times it will run
# for run in range(run_times):
#     print(next(it))


# Example 3: Iterate over a list and catch if overboards.
li = [100, 200, 300]
it = iter(li)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of Iteration")
        break  
