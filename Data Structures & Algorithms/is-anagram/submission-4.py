class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # iterate through first string
        # check the frequency of the character
        # if it's not equal to its frequency in the second string, return false
        # implitely return true

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for char in t:
            freq[char] = freq.get(char, 0) - 1

        for value in freq.values():
            if value > 0 or value < 0:
                return False
        
        return True