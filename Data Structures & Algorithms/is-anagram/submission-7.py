class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # just sort both string and check if they're equal

        return sorted(s) == sorted(t)