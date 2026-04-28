from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if not root:
            return []
        queue.append(root)
        levels = []
        while len(queue) > 0:
            cur_lvl = []  
            for _ in range(len(queue)):
                cur = queue.popleft()
                cur_lvl.append(cur.val)
                if  cur.left:
                    queue.append(cur.left)
                if  cur.right:
                    queue.append(cur.right)
            levels.append(cur_lvl)
        return levels

        