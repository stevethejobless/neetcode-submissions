# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def revLL(head, prevNode ):
            if head:
                nextNode = head.next
                head.next = prevNode
                prevNode = head
                head = nextNode
                return revLL(head, prevNode )
            else: return prevNode
        return revLL(head, None)
        