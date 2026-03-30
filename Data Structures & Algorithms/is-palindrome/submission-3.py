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

        while first < last:
            c1 = s[first].lower()
            c2 = s[last].lower()

            if not c1.isalnum():
                first += 1
            elif not c2.isalnum():
                last -= 1
            elif c1 != c2:
                return False
            else:
                first += 1
                last -= 1
        
        return True