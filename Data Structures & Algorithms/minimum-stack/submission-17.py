class MinStack:
    """
    Thought process
    - Keep two stacks; one our min_stack, stack
    - `min_stack` keeps all minimum valus. 
    - `stack` is the stack that keeps all values.
    - `push`; 
        - we check with top of min_stack. 
        - If element at top of min_stack is greater than new element, add to min_stack
        - Add value to stack
    - `pop`:
        - pop element of top of `stack`
        - check if element from stack equal the top of min_stack
        - If equal; pop otherwise continue
    - `top`:
        - simply return value at `stack[-1]`
    - `getMin`:
        - simply return value at `min_stack[-`]`

        Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

        Output: [null,null,null,null,0,null,2,1]

        Explanation:
        MinStack minStack = new MinStack();
        minStack.push(1);
        minStack.push(2);
        minStack.push(0);
        minStack.getMin(); // return 0
        minStack.pop();
        minStack.top();    // return 2
        minStack.getMin(); // return 1

        stack = [1, 2]
        min_stack = [1]
    """

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_stack.append(val)
            return
        
        if val <= self.min_stack[-1]:
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()

        if top == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
