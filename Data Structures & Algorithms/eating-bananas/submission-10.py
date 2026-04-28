import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)
        less = False

        while s<=e:
            k = (s+e)//2
            total_hours = sum([math.ceil(i/k) for i in piles])
            if total_hours > h:
                s = k+1
            elif total_hours <= h:
                e = k-1
        return k+1 if total_hours > h else k 

