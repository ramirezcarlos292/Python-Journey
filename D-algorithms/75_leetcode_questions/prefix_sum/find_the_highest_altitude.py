def largestAltitude(gain):
    currentaltitude = 0
    highestpoint = currentaltitude

    for altitude in gain:
        currentaltitude += altitude

        highestpoint = max(highestpoint, currentaltitude)

    return highestpoint
    


print(largestAltitude([-5,1,5,0,-7]))
# print(largestAltitude([-4,-3,-2,-1,4,3,2]))
# print(largestAltitude([52,-91,72]))