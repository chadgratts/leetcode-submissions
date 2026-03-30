class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # iterate through both strings
        # populate a dict, keys: chars, values: frequencies
        # example { c: 1, h: 1, a: 1, d:2 }
        # compare dictionaries

        freq_s = {}
        freq_t = {}

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        return freq_s == freq_t