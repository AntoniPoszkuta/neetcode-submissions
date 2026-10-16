# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swap_leafes(self, node):
        tmp = node.left
        node.left = node.right
        node.right = tmp
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            self.swap_leafes(root)
        return root