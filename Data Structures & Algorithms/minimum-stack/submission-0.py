class MinStack:

    def __init__(self):
        self.my_stack = []

    def push(self, val: int) -> None:
        min = val
        if self.my_stack:
            if val > self.my_stack[-1][1]:
                min = self.my_stack[-1][1]
            else:
                min = val
        self.my_stack.append([val, min])

    def pop(self) -> None:
        self.my_stack.pop()

    def top(self) -> int:
        return self.my_stack[-1][0]

    def getMin(self) -> int:
        return self.my_stack[-1][1]
        
