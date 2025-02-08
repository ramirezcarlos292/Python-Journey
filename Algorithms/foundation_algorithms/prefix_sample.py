# example: imagine arr is stroing the likes(+1) and dislikes (-1) of a given post
# we wanna know what the performance of the liking the post has, within a range 
# brute force would take a while, if elements are many so
arr = [8,3,-2,4,10,-1,0,5,3]
# with this, we will be precalculating the prefix sum of all elements

# create a prefix array filled in with zeros, of length == length of array
pfix = [0] * len(arr)

# assign first element of arr to be the first of prefix array
pfix[0] = arr[0]

# calculate each prefix sum per element in array, 0 index item was prev attached
for i in range(1, len(arr)):
    # sum prev prefix value to current array value
    pfix[i] = pfix[i - 1] + arr[i]

print(pfix)
assert pfix == [8, 11, 9, 13, 23, 22, 22, 27, 30]

# if wanna know how well the video did between day 2 and day 7
l = 2
r = 7
sum = pfix[7]-pfix[2-1]
print(sum)



## Better way of doing it, would be by adding an extra 0 to pfix sum, so whenever index 0 element
## is needed, the calculation does not get messes up negatively
p = [0] * (len(arr) + 1)
for i in range(1, len(arr)+1):
    p[i]  = p[i - 1] + arr[i - 1]
    
print(p[r+1]-p[l])