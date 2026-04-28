from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        q_len = len(self.q)
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()
        

    def top(self) -> int:
        temp_q = deque()
        while len(self.q) > 1:
            temp_q.appendleft(self.q.popleft())
        val = self.q[0]
        temp_q.appendleft(self.q.popleft())
        while len(temp_q):
            self.q.appendleft(temp_q.popleft())
        return val

    def empty(self) -> bool:
        return False if self.q else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()