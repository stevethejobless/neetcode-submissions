# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]], s=None, e=None) -> Optional[ListNode]:
        if s is e is None:
            s = 0
            e = len(lists) -1
        if e-s == 0:
            return lists[s]
        elif s > e:
            return None
        m = (s+e)//2
        L = self.mergeKLists(lists,s,m)
        R = self.mergeKLists(lists,m+1,e)
        return self.merge(L,R)
    
    def merge(self,L,R):
        D = ListNode(None,None)
        root = D
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
        elif R:
            D.next = R
        return root.next

    
    
        