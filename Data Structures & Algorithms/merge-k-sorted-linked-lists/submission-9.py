# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        for i in range(1, len(lists)):
            lists[i] = self.mergeLists(lists[i-1],lists[i])
        return lists[-1]


    def mergeLists(self,left,right):
        new = ListNode()
        res = new
        while left and right:
            if left.val > right.val:
                new.next = right
                right = right.next
            else:
                new.next = left
                left = left.next
            new = new.next
        new.next = left or right
        return res.next
