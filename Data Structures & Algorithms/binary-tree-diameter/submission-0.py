# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:


  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    max_diameter = 0

    def get_depth(node):

        if not node:
            return 0
        
        left = get_depth(node.left)
        right = get_depth(node.right)

        suma = right + left

        nonlocal max_diameter
        max_diameter = max(max_diameter, suma)

        return 1 + max(right, left)

    get_depth(root)
    return max_diameter