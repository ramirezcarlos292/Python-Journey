def kidsWithCandies(candies, extraCandies):
    record = []
    for i in range(len(candies)):
        num_candies = candies[i] + extraCandies
        if num_candies >= max(candies):
            record.append(True)
        else:
            record.append(False)
            

    return record


candies = [2,3,5,1,3]
extraCandies = 3

candies = [4,2,1,1,2]
extraCandies = 1

candies = [12,1,12]
extraCandies = 10

print(kidsWithCandies(candies, extraCandies))