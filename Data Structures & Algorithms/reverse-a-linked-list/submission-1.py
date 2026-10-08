# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = []
        while head != None:
            new.append(head.val)
            head = head.next
        
        new = new[::-1]
        if len(new) == 0:
            return head
        if len(new) == 1:
            return ListNode(new[0])
        head = ListNode(new[0])
        tmp = head
        for i in range(1,len(new)):
            tmp.next = ListNode(new[i])
            tmp = tmp.next
        return head