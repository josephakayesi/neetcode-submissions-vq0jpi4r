class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if not len(self.stack):
            self.stack.append(val)
            self.min_stack.append(val)
            return 

        min = self.min_stack[-1]

        if val <= min:
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        top = self.stack[-1]
        min = self.min_stack[-1]

        if top <= min:
            self.min_stack.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        

