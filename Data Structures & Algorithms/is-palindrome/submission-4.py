class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers, first and last indexes
        # loop while first < last
        # get first and last chars lowered
        # if first is not alphanum, increment
        # if last is not alphanum, decrement
        # if both don't match return False
        # move both
        # implicitely return True

        first = 0
        last = len(s) - 1

        while first < last:
            c1 = s[first].lower()
            c2 = s[last].lower()

            if not c1.isalnum():
                first += 1
                continue
            
            if not c2.isalnum():
                last -= 1
                continue
            
            if c1 != c2:
                return False
            
            first += 1
            last -= 1
        
        return True