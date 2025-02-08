import heapq

class Solution:
    def findRelativeRanks(score):
        n = len(score)
        ranks = ["Gold Medal","Silver Medal","Bronze Medal"]
        result = [""] * n
        heap = []
        for i in range(n):
            heap.append((-score[i], i))
        heapq.heapify(heap)
        print(heap)
        for rank in range(n):
            score, idx = heapq.heappop(heap)
            if rank < 3:
                result[idx] = ranks[rank]
            else:
                result[idx] = str(rank+1)
        return result

print(Solution.findRelativeRanks([5,4,3,2,1]))
print(Solution.findRelativeRanks([10,3,8,9,4]))
        
        
        