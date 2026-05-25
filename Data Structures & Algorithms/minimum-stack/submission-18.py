class MinStack:

    def __init__(self):
        self.stack = []
        self.min_list = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_list:
            self.min_list.append(val)
        else:
            min_val = min(self.min_list[-1], val)
            self.min_list.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_list.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_list[-1]