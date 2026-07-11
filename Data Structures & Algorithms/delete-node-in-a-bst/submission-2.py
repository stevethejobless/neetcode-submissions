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
        parent = None
        cur = root

        while cur and cur.val != key:
            parent = cur
            if val > cur.val:
                cur = cur.right
            if val < cur.val:
                cur = cur.left

        # Key Not Found
        if not cur:
            return root
        
        # One or no children
        if not cur.right or not cur.left:
            child = cur.right if cur.right else cur.left
            if not parent:
                return child
            if parent.right == cur:
                parent.right = child
            else:
                parent.left = child
        
        else:
            del_node = cur
            min_par = None  # Parent of min node
            cur = cur.right

            while cur.left:
                min_par = cur
                cur = cur.left
            
            if min_par:
                min_par.left = cur.right
                cur.right = del_node.right
                
            cur.left = del_node.left
            if not parent:
                return cur
            if parent.left == del_node:
                parent.left = cur
            else:
                parent.right = cur
        
        return root
