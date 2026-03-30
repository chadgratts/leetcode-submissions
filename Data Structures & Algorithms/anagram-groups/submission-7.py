class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        make result dict
        iterate through strs list
        make empty signature [0...] 26 zeros, one for each alphabet char
        iterate through the current string
        create signature by mutating the list of zeros. for each char, find its
        position in the signature and increment its frequency
        turn signature into a tuple
        if it's not in result, add empty list
        add the current string to the value of its' signature in result
        return a list of results' values
        
        """
        result = {}

        for s in strs:
            signature = [0] * 26

            for char in s:
                signature[ord(char) - ord("a")] += 1
            
            key = tuple(signature)
            if key not in result:
                result[key] = []
            result[key] += [s]

        return list(result.values())