class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # just sort both strings and check if they're equal

        # return sorted(s) == sorted(t)

        # Time complexity: idk what it is from running sort
        # Space complexity: i think none 0

        letters = list(max(s, t, key=len))

        for letter in letters:
            if s.count(letter) != t.count(letter):
                return False
        
        return True