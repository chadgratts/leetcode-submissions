class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_b = ["[", "(", "{"]
        close_b = ["]", ")", "}"]
        pairs = ["[]", "()", "{}"]

        for b in s:
            print(stack)
            if b in open_b:
                stack.append(b)
            elif b in close_b:
                if not stack:
                    return False
                elif stack[-1] in open_b and stack[-1] + b in pairs:
                    print(stack, f'->{b}')
                    stack.pop()
                else:
                    return False

        return len(stack) == 0