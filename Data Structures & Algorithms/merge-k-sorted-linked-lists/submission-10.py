# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [(node.val,i,node) for i,node in enumerate(lists)]
        print(lists)
        heapq.heapify(lists)
        new = ListNode()
        res = new
        while lists:
            node = heapq.heappop(lists)
            new.next = node[2]
            new = new.next
            next_node = node[2].next
            if next_node:
                heapq.heappush(lists,(next_node.val,node[1],next_node))
        return(res.next)

        
