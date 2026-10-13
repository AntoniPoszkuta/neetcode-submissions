"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next, None)
            cur = cur.next.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        copy = head.next
        copy_head = copy
        while cur:
            cur.next = cur.next.next
            cur = cur.next
            if copy.next:
                copy.next = copy.next.next
                copy = copy.next
        return copy_head