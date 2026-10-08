# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list2 == None and list1 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        if list1.val > list2.val:
            merged = ListNode(list2.val)
            list2 = list2.next
        else:
            merged = ListNode(list1.val)
            list1 = list1.next

        head = merged

        while list1 != None and list2 != None:
            if list1.val > list2.val:
                merged.next = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                merged.next = list1
                list1 = list1.next
            
            merged = merged.next

        if list1 != None:
            merged.next = list1

        if list2 != None:
            merged.next = list2

        return head