class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for string in strs:
            frequencies = [0] * 26

            for char in string:
                frequencies[ord(char) - ord('a')] += 1
        
            key = tuple(frequencies)

            if key in group:
                group[key].append(string)
            else:
                group[key] = [string]
        
        return list(group.values())