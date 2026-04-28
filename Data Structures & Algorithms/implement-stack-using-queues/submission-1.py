from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        temp_q = deque()
        while len(self.q) > 1:
            temp_q.append(self.q.popleft())
        val = self.q.popleft()
        self.q = temp_q
        return val

    def top(self) -> int:
        temp_q = deque()
        while len(self.q) > 1:
            temp_q.append(self.q.popleft())
        val = self.q[0]
        temp_q.append(self.q.popleft())
        self.q = temp_q
        return val

    def empty(self) -> bool:
        return False if self.q else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()