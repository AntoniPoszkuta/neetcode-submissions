# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True

        def isValid(node, left_bound, right_bound):
            nonlocal valid
            if not node or not valid:
                return
            if node.val > left_bound and node.val < right_bound:
                isValid(node.left,left_bound,node.val)
                isValid(node.right,node.val,right_bound)
            else:
                valid = False
        
        isValid(root, float('-inf'), float('inf'))
        return valid