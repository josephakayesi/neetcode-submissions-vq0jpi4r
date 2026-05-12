class MinStack:
    """
        # 1. check if min stack is empty
        # 2. If empty; push val
        # 3. If not empty; compare top of min stack with val
        # 4. If val < top:
        #       push to minstack
        #   else do nothing

        # Not empty
    """

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # if not self.minStack:
        #     self.minStack.append(val)
        #     return 
        
        # if val <= self.minStack[-1]:
        #     self.minStack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
            self.minStack.append(val)


    def pop(self) -> None:
        last = self.stack.pop()

        if last == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
