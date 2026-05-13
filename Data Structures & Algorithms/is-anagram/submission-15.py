class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqs = {}

        for ch in s:
            freqs[ch] = freqs.get(ch, 0) + 1
        
        for ch in t:
            freqs[ch] = freqs.get(ch, 0) - 1

            if freqs[ch] < 0:
                return False
        return True