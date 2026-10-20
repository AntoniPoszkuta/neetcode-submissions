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
            if not valid:
                return
            
            if node.left:
                if node.left.val < node.val:
                    isValid(node.left)
                else:
                    valid = False

            if node.right:
                if node.right.val > node.val:
                    isValid(node.right)
                else:
                    valid = False
                
        isValid(root)
        return valid