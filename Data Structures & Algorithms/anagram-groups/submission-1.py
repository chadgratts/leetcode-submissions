class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for word in strs:
            freqs = [0] * 26

            for char in word:
                freqs[ord(char) - ord('a')] += 1
            
            freqs = tuple(freqs)

            if freqs not in anagram:
                anagram[freqs] = []
            
            anagram[freqs].append(word)
        
        return list(anagram.values())