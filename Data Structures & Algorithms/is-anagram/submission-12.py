class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        f = {}

        for ch in s:
            f[ch] = f.get(ch, 0) + 1
        
        for ch in t:
            f[ch] = f.get(ch, 0) - 1
        
        for f in f.values():
            if f != 0:
                return False
        
        return True
