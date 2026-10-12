# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        res = head
        
        mid = False

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow.next
        slow.next = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp


        # poczatek : head, polowa : prev
        cur_1 = head
        cur_2 = prev
        while cur_2:
            tmp = cur_1.next
            cur_1.next = cur_2
            tmp_2 = cur_2.next
            cur_2.next = tmp
            cur_1, cur_2 = tmp, tmp_2
        
            