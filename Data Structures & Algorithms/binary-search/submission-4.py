class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)
        m = (s+e)//2
        while e>=s and m<len(nums):
            if target > nums[m]:
                s = m+1
            elif target < nums[m]:
                e = m-1
            else:
                return m
            m = (s+e)//2
        return -1
        