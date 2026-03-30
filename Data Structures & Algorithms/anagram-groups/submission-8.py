class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            serialization = [0] * 26

            for c in s:
                serialization[ord(c) - ord("a")] += 1
            
            key = tuple(serialization)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        
        return list(groups.values())