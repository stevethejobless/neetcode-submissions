class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def popper(i, nums):
            if i <= len(nums) - 2:
                if(nums[i] == nums[i+1]):
                    for j in range(i+1, len(nums)-1):
                        nums[j] = nums[j+1]
                    del nums[len(nums) - 1]
                    popper(i, nums)
                else:
                    popper(i+1, nums)
            else: return nums
        popper(0,nums)
        print(nums)
        return len(nums)
        