# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True

        def get_depth(node):

            nonlocal balance

            if not balance:
                return 0

            if not node:
                return 0
            
            left = get_depth(node.left)
            right = get_depth(node.right)

            if abs(left - right) > 1:
                balance = False
            
            return 1 + max(left, right)

        get_depth(root)
        return balance