class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for b in s:
            if b not in pairs:
                stack.append(b)
            elif stack and pairs[b] == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack