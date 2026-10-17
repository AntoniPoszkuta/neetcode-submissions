from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue_one = deque()
        queue_two = deque()

        if not q or not p:
            return True
        
        queue_one.append(p)
        queue_two.append(q)

        while queue_one and queue_two:
            level_one = len(queue_one)
            level_two = len(queue_two)

            if level_one != level_two:
                return False

            for _ in range(level_one):
                node1 = queue_one.popleft()
                node2 = queue_two.popleft()

                if node1.val != node2.val:
                    return False
                if (node1.left and not node2.left) or (node1.right and not node2.right) or (node2.left and not node1.left) or (node2.right and not node1.right):
                    return False
                if node1.left and node1.left.val != node2.left.val:
                    return False
                if node1.right and node1.right.val != node2.right.val:
                    return False
                if node1.left:
                    queue_one.append(node1.left)
                if node1.right:
                    queue_one.append(node1.right)
                if node2.left:
                    queue_two.append(node2.left)
                if node2.right:
                    queue_two.append(node2.right)

        return True if len(queue_one) == len(queue_two) else False