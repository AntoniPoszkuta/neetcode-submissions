# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = None

        def Ancestor(node,p,q):
            nonlocal ancestor
            if not ancestor:
                if p.val > node.val and q.val > node.val:
                    Ancestor(node.right,p,q)
                elif p.val < node.val and q.val < node.val:
                    Ancestor(node.left,p,q)
                else:
                    ancestor = node
        
        Ancestor(root,p,q)
        return ancestor
                