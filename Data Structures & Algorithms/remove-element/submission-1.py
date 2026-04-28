class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_index, val_index_inv = [], []
        for i in range(len(nums)):
            if nums[i] == val:
                val_index.append(i)
            else: val_index_inv.append(i)
        if len(val_index_inv) == 0:
            return 0
        for i in range(len(val_index)):
            if val_index[i] < val_index_inv[-(i+1)]:
                nums[val_index[i]] = nums[val_index_inv[-(i+1)]]
            else: break
        return len(val_index_inv)