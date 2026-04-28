class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_index, j, k = [], 0, 0
        for i in range(len(nums)):
            if nums[i] == val:
                val_index.append(i)
                k+=1
            elif len(val_index) > 0:
                nums[val_index[j]] = nums[i] 
                val_index.append(i)
                j+=1
        return len(nums) - k