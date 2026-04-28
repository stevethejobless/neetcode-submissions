import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)
        res=None
        while s<=e:
            k = (s+e)//2
            total_hours = sum(math.ceil(i/k) for i in piles)
            if total_hours <= h:
                e = k-1
                res = k
            else: s=k+1
        return res

