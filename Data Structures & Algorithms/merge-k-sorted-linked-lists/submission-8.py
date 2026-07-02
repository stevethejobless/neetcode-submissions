# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        while True:
            min_node = None
            for i in range(0,len(lists)):
                if not lists[i]:
                    continue
                if min_node == None or lists[min_node].val > lists[i].val:
                    min_node = i
            if min_node == None:
                break
            cur.next = lists[min_node]
            lists[min_node] = lists[min_node].next
            cur = cur.next
        return res.next  
        
