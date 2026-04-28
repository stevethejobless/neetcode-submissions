class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)
        ans = [None]*len(nums)*2
        for _ in range(len(nums)):
            ans[i] = nums[i]
            ans[j] = nums[i]
            i+=1
            j+=1
        return ans