class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,num in enumerate(nums):
            if hash_map.get(target-num) is not None:
                return [hash_map[target-num],i]
            hash_map[num] = i