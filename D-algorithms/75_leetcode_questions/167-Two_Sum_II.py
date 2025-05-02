from typing import List
class Solution:
    def two_sum_II(numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l <= r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l, r]
            if summ > target:
                r -= 1
            else:
                l += 1
    


print(Solution.two_sum_II([2,7,11,15], 9))