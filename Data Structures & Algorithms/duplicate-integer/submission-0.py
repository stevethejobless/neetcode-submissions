class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else: return True
        return False