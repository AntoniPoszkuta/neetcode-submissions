# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        one_cycler = head
        two_cycler = head
        while one_cycler and two_cycler:
            one_cycler = one_cycler.next
            two_cycler = two_cycler.next
            if not two_cycler or not one_cycler:
                return False
            two_cycler = two_cycler.next
            if not two_cycler:
                return False
            elif two_cycler == one_cycler:
                return True

        return False
