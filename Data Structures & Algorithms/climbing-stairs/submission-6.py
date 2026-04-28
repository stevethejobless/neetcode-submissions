class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev1 = 2
        steps = n
        if n <=2:
            return n
        for i in range(3,n+1):
            steps = prev1 + prev2
            prev2 = prev1
            prev1 = steps
        return steps