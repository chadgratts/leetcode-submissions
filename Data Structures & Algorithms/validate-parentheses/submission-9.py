class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        for char in s:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]: # "(" in stack and stack[char] gives me "("
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
