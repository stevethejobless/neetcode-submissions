class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j+=1
        nums[j] = nums[len(nums) - 1]
        return j+1