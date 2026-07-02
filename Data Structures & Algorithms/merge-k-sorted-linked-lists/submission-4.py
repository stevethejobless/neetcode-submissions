# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_list = []
        for i in lists:
            while i:
                dummy_list.append(i.val)
                i = i.next
        dummy_list.sort()
        new_list = ListNode()
        head = new_list
        for i in dummy_list:
            new_list.next = ListNode(i)
            new_list = new_list.next
        return head.next
        
        
