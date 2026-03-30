class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate through strings
        # create sublist
        # nested loop at i + 1 to the end to find other anagrams
        # check if the two strings are anagrams
        #   create frequency hash
        #   iterate through both strings,
        #     first string increments, second string decrements
        #     iterate through the frequency hash, each value should be 0
        # if they are, add the string from the nested loop to the subarray
        # after the nested loops runs, add the subarray to the resut array if its len is > 0

        result = []
        used = set()

        for i in range(len(strs)):
            if i in used:
                continue
            
            sublist = [strs[i]]
            used.add(i)

            for j in range(i + 1, len(strs)):
                if j in used:
                    continue

                freq = {}
                for char in strs[i]:
                    freq[char] = freq.get(char, 0) + 1
                for char in strs[j]:
                    freq[char] = freq.get(char, 0) - 1

                is_anagram = True
                for v in freq.values():
                    if v != 0:
                        is_anagram = False
                        break

                if is_anagram:
                    sublist.append(strs[j])
                    used.add(j)

            result.append(sublist)
        
        return result
