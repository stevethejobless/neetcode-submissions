# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, pathSum=None) -> bool:
        if not root:
            return False
        if pathSum is None:
            pathSum = root.val
        else: pathSum+=root.val
        if not root.left and not root.right:
            return True if pathSum == targetSum else False
        if root.left and self.hasPathSum(root.left,targetSum,pathSum):
            return True
        if root.right and self.hasPathSum(root.right, targetSum, pathSum):
            return True
        return False



        