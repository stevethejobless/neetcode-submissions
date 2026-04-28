class MinStack:

    def __init__(self):
        self.minVal = 0
        self.stack = [] 

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minVal = val
        else:
            self.stack.append(val - self.minVal)
            if val - self.minVal < 0:
                self.minVal = val

    def pop(self) -> None:
        lastVal = self.stack.pop()
        if lastVal < 0:
            self.minVal = self.minVal - lastVal
        

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.minVal
        else:
            return self.stack[-1] + self.minVal
        

    def getMin(self) -> int:
        return self.minVal
