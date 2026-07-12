# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        if key == root.val:
            if not root.right or not root.left:
                return root.right if root.right else root.left
            cur = root.right
            res = cur
            while cur.left:
                cur = cur.left
            cur.left = root.left
            del root
            return res
        return root