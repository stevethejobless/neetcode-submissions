# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divide(lists,0,len(lists)-1)
        
    def divide(self,lists, s, e):
        if s == e:
            return lists[s]
        m = (s+e)//2
        print(s,m,e)
        L = self.divide(lists, s,m)
        R = self.divide(lists, m+1, e)
        return self.merge(L,R)
    
    def merge(self,L,R):
        new = ListNode()
        root = new
        while L and R:
            if L.val < R.val:
                new.next = L
                L = L.next
            else:
                new.next = R
                R = R.next
            new = new.next
        new.next = L or R
        return root.next