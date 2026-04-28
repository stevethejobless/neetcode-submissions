class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        while e>=s:
            m = (s+e)//2
            if target > nums[m]:
                s = m+1
            elif target < nums[m]:
                e = m-1
            else:
                return m
        return -1
        