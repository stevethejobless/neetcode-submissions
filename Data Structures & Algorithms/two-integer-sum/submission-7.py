class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i,j in enumerate(nums):
            A.append((j,i))
        A.sort()
        i = 0
        j = len(nums) - 1
        while i<len(nums) and j>-1:
            if A[i][0] + A[j][0] < target:
                i +=1
            elif A[i][0] + A[j][0] > target:
                j-=1
            else:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]