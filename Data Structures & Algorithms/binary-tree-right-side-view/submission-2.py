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
        right_view = []
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            level_len = len(queue)
            for i in range(len(queue)):
                cur = queue.popleft()
                if i == level_len -1:
                    right_view.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return right_view

