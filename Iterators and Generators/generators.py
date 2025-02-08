### https://www.geeksforgeeks.org/generators-in-python/

# A generator function is a special function that 
# returns an iterator object. Use yield keyword instead of return

# Example 1: 
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1
        

ctr = fun(5)
for n in ctr:
    print(n) 
    
# Example 2: Custom Generator
def fun():
    yield 1
    yield 2
    yield 3
    
for val in fun():
    print(val)


sq = (x*x for x in range(1, 2))
for i in sq:
    print(i)