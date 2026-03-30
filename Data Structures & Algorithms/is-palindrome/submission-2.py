class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create two pointers, first and last
        # loop while first <= last
        # if first is not alphanumeric, increment it
        # if last is not alphanumeric, decrement it
        # if they are not the same alphanum, return false
        # increment/decrement both
        # implicitly return True

        first = 0
        last = len(s) - 1
        alphanum = "abcdefghijklmnopqrstuvwxyz1234567890"

        while first < last:
            if not s[first].isalnum():
                first += 1
            elif not s[last].isalnum():
                last -= 1
            elif s[first].lower() != s[last].lower():
                return False
            else:
                first += 1
                last -= 1
        
        return True