class Node:
    def __init__(self,key=None,val=None,next=None,prev=None):
        self.key,self.val = key,val
        self.next,self.prev = next,prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head,self.tail = Node(),Node()
        self.head.next,self.tail.prev = self.tail, self.head
    
    def _remove(self,key):
        prev, next = self.cache[key].prev , self.cache[key].next
        print(key,prev,next)
        prev.next, next.prev = next, prev
    
    def _insert(self,key):
        prev = self.tail.prev
        prev.next, self.cache[key].prev = self.cache[key], prev
        self.tail.prev,self.cache[key].next = self.cache[key],self.tail
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(key)
            self._insert(key)
            return self.cache[key].val
        return -1
        

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.cache[key].val = val
            self._remove(key)
            self._insert(key)
        else:
            if len(self.cache) >= self.cap:
                lru = self.head.next.key
                self._remove(lru)
                del self.cache[lru]
            self.cache[key] = Node(key=key,val=val)
            self._insert(key)
                

        
