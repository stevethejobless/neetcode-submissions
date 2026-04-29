class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,subset,total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(nums):
                return
            
            # Decision to include
            subset.append(nums[i])
            dfs(i,subset,total+nums[i])

            # Decision to not include
            subset.pop()
            dfs(i+1,subset,total)
        dfs(0,[],0)
        return res