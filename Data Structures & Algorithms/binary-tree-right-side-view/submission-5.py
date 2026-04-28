# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        def dfs(root, cur_lvl):
            if not root:
                return
            if cur_lvl == len(right_view):
                right_view.append(root.val)
            dfs(root.right,cur_lvl +1)
            dfs(root.left, cur_lvl + 1)
        dfs(root,0)
        return right_view