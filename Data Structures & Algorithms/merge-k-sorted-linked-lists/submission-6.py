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
            min_node_index = None
            for i,node in enumerate(lists):
                if not node:
                    continue
                if (not min_node) or (min_node.val > node.val):
                    min_node = node
                    min_node_index = i
            if not min_node:
                break
            cur.next = min_node
            cur = cur.next
            lists[min_node_index] = lists[min_node_index].next
        return res.next
        
