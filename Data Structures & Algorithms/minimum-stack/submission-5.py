class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = 0

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.mini = val
            self.stack.append(0)
        else:
            diff = val - self.mini
            self.stack.append(diff)
            if diff < 0:
                self.mini = val

    def pop(self) -> None:
        last = self.stack.pop()
        if last < 0:
            self.mini = self.mini - last

    def top(self) -> int:
        last = self.stack[-1]
        if last < 0:
            return self.mini
        else:
            return last + self.mini


    def getMin(self) -> int:
        return self.mini
