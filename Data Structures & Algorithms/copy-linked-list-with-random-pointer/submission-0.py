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
        dic = {}
        tmp = head
        new_head = Node(tmp.val, None, None)
        dic[tmp] = new_head
        tmp = tmp.next
        while tmp:
            dic[tmp] = Node(tmp.val, None, None)
            tmp = tmp.next
        
        tmp = head
        while tmp:
            dic[tmp].next = dic.get(tmp.next)
            dic[tmp].random = dic.get(tmp.random)
            tmp = tmp.next
        return new_head
        