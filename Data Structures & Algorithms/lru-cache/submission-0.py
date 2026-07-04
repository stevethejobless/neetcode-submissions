class ListNode:
    def __init__(self,key=None,val=None,prev=None,next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_size = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        res = self.cache.get(key,ListNode(val=-1))
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self._insert_at_head(key,res.val)
            self.cache[key] = self.head.next
        return res.val
     

    def put(self, key: int, val: int) -> None:
        if key not in self.cache:
            if len(self.cache) < self.cache_size:
                self._insert_at_head(key,val)
            else:
                least_prio = self.tail.prev
                least_prio.prev.next = self.tail
                self.tail.prev = least_prio.prev
                del self.cache[least_prio.key]
                self._insert_at_head(key,val)
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self._insert_at_head(key,val)
            self.cache[key] = self.head.next
    
    def _insert_at_head(self,key,val):
        self.cache[key] = ListNode(key,val)
        next_node = self.head.next
        self.head.next = self.cache[key]
        self.cache[key].prev = self.head
        self.cache[key].next = next_node
        next_node.prev = self.cache[key]




        
