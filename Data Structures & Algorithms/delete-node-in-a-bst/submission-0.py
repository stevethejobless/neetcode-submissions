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
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            min_node = self.findMin(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right,min_node.val)
        return root
    
    def findMin(self,root):
        while root:
            if not root.left:
                return root
            root = root.left
        