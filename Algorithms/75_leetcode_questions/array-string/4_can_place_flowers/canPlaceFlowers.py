class Solution:
    def canPlaceFlowers(flowerbed, n):
        ## add zeroes to original array, -1 and at the end of array
        f = [0] + flowerbed + [0]
        
        ## iterate over array avoiding added items, starts 1 and end + 1 cuz started at zero
        for i in range(1, len(flowerbed)+1):
            ## check if 3 contiguous elemets are 0
            if (f[i-1] == 0) and (f[i] == 0) and (f[i+1] == 0):
                ## if yes, change middle item to be 1 on the array
                f[i] = 1
                ## decrease by one n(plants to be planted)
                n -= 1
        ## if the for loop ends and n > 0, means not all plants could be planted, thus return evaluates False
        ## on the contrary if n <= 0, means all plants were planted and return evaluates as True
        return n <= 0
            
                


flowerbed = [1,0,0,0,1]
# print(Solution.canPlaceFlowers(flowerbed, 1))
print(Solution.canPlaceFlowers(flowerbed, 2))