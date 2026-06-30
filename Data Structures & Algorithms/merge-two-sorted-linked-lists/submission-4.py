# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = ListNode()
        head = sorted_list
        while list1 and list2:
            if list1.val <= list2.val:
                sorted_list.next = list1
                list1 = list1.next
            else:
                sorted_list.next = list2
                list2 = list2.next
            sorted_list = sorted_list.next
        sorted_list.next = list2 if list2 else list1 if list1 else None
        return head.next