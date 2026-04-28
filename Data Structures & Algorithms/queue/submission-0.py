class Node:
    def __init__(self,val=None,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
class Deque:
    
    def __init__(self):
        self.head = self.tail = None


    def isEmpty(self) -> bool:
        if self.head == self.tail == None:
            return True
        return False

    def append(self, value: int) -> None:
        node = Node(value)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        

    def appendleft(self, value: int) -> None:
        node = Node(value)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            val = self.tail.val
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                temp = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                temp.prev = None
            return val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            val = self.head.val
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                temp = self.head
                self.head = self.head.next
                self.head.prev = None
                temp.next = None
            return val

        
