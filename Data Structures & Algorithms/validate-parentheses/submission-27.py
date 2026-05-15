class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = { ')': '(', '}': '{', ']': '[' }

        for brack in s:
            if brack not in brackets:
                stack.append(brack)
            elif stack and stack[-1] == brackets[brack]:
                stack.pop()
            else:
                return False
        return not stack