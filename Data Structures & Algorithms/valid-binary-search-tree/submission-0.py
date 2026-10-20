# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        valid = True

        def isValid(node):
            nonlocal valid
            if valid:
                if node.left and node.left.val < node.val:
                    isValid(node.left)
                elif node.left and node.left.val >= node.val:
                    valid = False

                if node.right and node.right.val > node.val:
                    isValid(node.right)
                elif node.right and node.right.val <= node.val:
                    valid = False
                
        isValid(root)
        return valid