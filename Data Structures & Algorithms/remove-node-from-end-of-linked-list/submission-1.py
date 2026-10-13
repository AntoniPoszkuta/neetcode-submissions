# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        if length == 0:
            return head
        if length == 1 and n == 1:
            return None
        if n == length:
            head = head.next
            return head

        cur = head
        for _ in range(length - n - 1):
            cur = cur.next

        if cur.next and cur.next.next:
            cur.next = cur.next.next
        elif cur.next:
            cur.next = None
        
        return head