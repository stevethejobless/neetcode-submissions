# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if len(lists) <=0:
            return None
        m = len(lists)//2
        L = self.mergeKLists(lists[0:m])
        R = self.mergeKLists(lists[m:len(lists)])
        return self.merge(L,R)
    
    def merge(self,L,R):
        D = ListNode(None,None)
        head = D
        while L and R:
            if L.val <= R.val:
                D.next = L
                L = L.next
                D = D.next
            else:
                D.next = R
                R = R.next
                D = D.next
        if L:
            D.next = L
        if R:
            D.next = R
        return head.next
