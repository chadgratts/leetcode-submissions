class MinStack():
    """
    Identify the pattern - stack, keep track of min
    Say the recognition cue - always can get min, even after popping and pushing
    State the key insight - when pushing, add to stack and min stack, so you keep state of at any point in the stack when you have x elements, the top of the stack is the current min. 
        Define the invariant - the top of the min stack is always the min. even after popping. because we always add to the min value to the min stack during push. in other words, after every push, we add the min so far, to the min stack. both lists are in line with each other. the min stack always has the min so far, since both are pushed and popped together.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if self.min_stack:
            current_min = min(self.min_stack[-1], val)
            self.min_stack.append(current_min)
        else:
            self.min_stack.append(val)
        

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()