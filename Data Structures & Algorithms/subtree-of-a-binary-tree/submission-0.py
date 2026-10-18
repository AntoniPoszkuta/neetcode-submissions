# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSame(self, a, b):
        if not a and not b:
            return True
        
        if not a or not b or a.val != b.val:
            return False

        return self.isSame(a.left, b.left) and self.isSame(a.right, b.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        is_sub = False

        def isSub(node, sub):
            nonlocal is_sub
            if not is_sub and node:
                if node.val == sub.val:
                    is_sub = self.isSame(node, sub)
                isSub(node.left, sub)
                isSub(node.right, sub)
        
        isSub(root, subRoot)

        return is_sub