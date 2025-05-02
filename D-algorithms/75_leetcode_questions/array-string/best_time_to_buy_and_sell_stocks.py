def maxProfit(prices):
    k = 1
    lowest = 0
    highest = 0 
    for i , item in enumerate(prices):
        #end of list?
        if i == len(prices):
            break
        # is item lower than next?
        # if yes, store as buy candidate, then go next
        if item < prices[i+k]:
            print(item)
        else:
            k+=1
            
        
        # if not, go to next
prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]

maxProfit(prices)