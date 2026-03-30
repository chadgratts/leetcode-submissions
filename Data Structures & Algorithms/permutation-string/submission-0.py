from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        if m > len(s2):
            return False
        
        need = Counter(s1)
        window = Counter(s2[:m])

        if window == need:
            return True
        
        for r in range(m, len(s2)):
            window[s2[r]] += 1
            window[s2[r - m]] -= 1

            if window[s2[r - m]] == 0:
                del window[s2[r - m]]

            if window == need:
                return True

        return False