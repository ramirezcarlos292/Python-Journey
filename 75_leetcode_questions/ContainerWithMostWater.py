def maxArea(heights):
    n = len(heights)
    for i in range(n):
        for j in range(1, n-1):
            print(heights[j])

maxArea([1,7,2,5,4,7,3,6])