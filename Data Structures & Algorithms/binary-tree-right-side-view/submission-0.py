from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels = []
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            cur_level = []
            for i in range(len(queue)):
                cur = queue.popleft()
                cur_level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            levels.append(cur_level)
        right_view = []
        for i in levels:
            right_view.append(i[-1])
        return right_view

