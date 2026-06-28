class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_srt = nums.copy()
        nums_srt.sort()
        i = 0
        j = len(nums) - 1
        while i<len(nums) and j>=0:
            if nums_srt[i] + nums_srt[j] > target:
                j-=1
            elif nums_srt[i] + nums_srt[j] < target:
                i+=1
            else:
                if nums.index(nums_srt[i]) < nums.index(nums_srt[j]):
                    return [nums.index(nums_srt[i]),nums.index(nums_srt[j])]
                elif nums.index(nums_srt[i]) > nums.index(nums_srt[j]):
                    return [nums.index(nums_srt[j]),nums.index(nums_srt[i])]
                else:
                    return [nums.index(nums_srt[i]),
                            nums.index(nums_srt[i],nums.index(nums_srt[i])+1)]
        
