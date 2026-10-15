# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,None)
        dummy_head = dummy
        extra = 0
        while l1 or l2 or extra:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            new_sum = first + second + extra
            extra = new_sum // 10
            dummy.next = ListNode(new_sum % 10, None)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            dummy = dummy.next
        return dummy_head.next