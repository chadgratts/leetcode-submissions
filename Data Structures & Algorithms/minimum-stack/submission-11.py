class MinStack:

    def __init__(self):
        self.q = deque()
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)

        self.q.appendleft(val)

    def pop(self) -> None:
        val = self.q.popleft()
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self) -> int:
        return self.q[0] if self.q else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else -3
