class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min = val
            self.stack.append(0)
            return
        diff = val - self.min
        if diff>=0:
            self.stack.append(diff)
        else:
            self.stack.append(diff)
            self.min = val
        print('pushed', self.stack, self.min)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped < 0:
            self.min = self.min - popped
        print('popped',self.stack, self.min)

    def top(self) -> int:
        last = self.stack[-1]
        if last < 0:
            return self.min
        return last + self.min

    def getMin(self) -> int:
        return self.min
        
