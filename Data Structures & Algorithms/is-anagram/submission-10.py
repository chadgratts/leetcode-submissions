class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # just sort both strings and check if they're equal

        # return sorted(s) == sorted(t)

        # Time complexity: idk what it is from running sort (python sort is O(nlogn))
        # Space complexity: i think none 0

        # letters = list(max(s, t, key=len))

        # for letter in letters:
        #     if s.count(letter) != t.count(letter):
        #         return False
        
        # return True

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for char in t:
            freq[char] = freq.get(char, 0) - 1
        
        for freq in freq.values():
            if freq != 0:
                return False
        return True