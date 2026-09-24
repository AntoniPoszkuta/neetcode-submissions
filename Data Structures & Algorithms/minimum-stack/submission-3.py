class MinStack:

    def __init__(self):
        self.mins = [] 
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        elif self.mins[-1] < val:
            self.mins.append(self.mins[-1])
        else:
            self.mins.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]