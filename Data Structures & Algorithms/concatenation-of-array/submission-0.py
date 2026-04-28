class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None]*len(nums)*2
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
        return ans