class MinStack:

    def __init__(self):
        self.q = deque()

    def push(self, val: int) -> None:
        self.q.appendleft(val)

    def pop(self) -> None:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0] if self.q else None

    def getMin(self) -> int:
        return min(self.q)
