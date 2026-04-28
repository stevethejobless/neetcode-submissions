# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        def dfs(root,cur_lvl):
            if not root:
                return
            nonlocal levels
            print(root.val,len(levels),cur_lvl)
            if len(levels) < cur_lvl+1:
                levels.append([root.val])
            else:
                levels[cur_lvl].append(root.val)
            dfs(root.left,cur_lvl+1)
            dfs(root.right,cur_lvl+1)
        dfs(root,0)
        return levels
        