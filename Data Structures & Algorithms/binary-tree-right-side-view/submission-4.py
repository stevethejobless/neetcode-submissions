# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        lvl_map = {}
        def dfs(root, cur_lvl, lvl_map):
            if not root:
                return
            dfs(root.right,cur_lvl +1, lvl_map)
            if not lvl_map.get(cur_lvl):
                lvl_map[cur_lvl] = root.val
            dfs(root.left, cur_lvl + 1, lvl_map)
        dfs(root,0,lvl_map)
        return [lvl_map[i] for i in range(len(lvl_map))]
            