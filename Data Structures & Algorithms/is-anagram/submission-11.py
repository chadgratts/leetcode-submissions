class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencies = {}

        for char in s:
            frequencies[char] = frequencies.get(char, 0) + 1

        for char in t:
            frequencies[char] = frequencies.get(char, 0) - 1
        
        for v in frequencies.values():
            if v != 0:
                return False
        
        return True