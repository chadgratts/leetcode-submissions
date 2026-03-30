class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # [

        for char in s:
            if char not in [")", "]", "}"]: # if char is an open bracket
                stack.append(char)
            else: # its a closing bracket
                if not stack:
                    return False
                bracket = stack.pop()
                if bracket + char not in ["()", "[]", "{}"]:
                    return False
                    
        return not stack