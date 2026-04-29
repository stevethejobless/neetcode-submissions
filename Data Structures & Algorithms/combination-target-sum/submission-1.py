class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(cur):
            subset.append(cur)
            if sum(subset) >= target:
                if sum(subset) == target:
                    sorted_subset = subset.copy()
                    sorted_subset.sort()
                    if sorted_subset not in res:
                        res.append(sorted_subset)    
                subset.pop()
                return
            for i in nums:
                dfs(i)
            subset.pop()
        index = 0
        while len(nums) > 0:
            dfs(nums[-1])
            nums.pop()
        return res