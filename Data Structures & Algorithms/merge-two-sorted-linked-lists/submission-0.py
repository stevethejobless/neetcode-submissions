# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and list2:
            return []
        
        if list1.val <= list2.val:
            firstNode = list1
            secondNode = list2
            head = list1
        else:
            firstNode = list2
            secondNode = list1
            head = list2
        
        while firstNode.next:
            if firstNode.next.val <= secondNode.val:
                firstNode = firstNode.next
            else:
                temp = firstNode.next
                firstNode.next = secondNode
                firstNode = secondNode
                secondNode = temp
        firstNode.next = secondNode
        return head
