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
        
        cur = root
        parent = None
        while cur and cur.val != key:
            parent = cur
            if key > cur.val:
                cur = cur.right
            if key < cur.val:
                cur = cur.left
        
        if not cur:
            return root

        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not parent:
                return child
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
            return root
        
        del_node = cur
        cur = cur.right
        while cur.left:
            cur = cur.left
        cur.left = del_node.left
        if parent:
            if parent.left == del_node:
                parent.left = del_node.right
            else:
                parent.right = del_node.right
            return root
        else:
            return del_node.right
    
