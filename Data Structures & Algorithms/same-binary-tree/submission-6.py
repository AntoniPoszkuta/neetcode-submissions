# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        is_same = True

        def check_nodes(p, q):
            nonlocal is_same

            if not p and not q:
                pass
            elif not p or not q or q.val != p.val:
                is_same = False
            else:
                check_nodes(p.left,q.left)
                check_nodes(p.right,q.right)
                
        check_nodes(p,q)
        
        return is_same