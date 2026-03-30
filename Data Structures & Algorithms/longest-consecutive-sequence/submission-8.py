class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for x in s:
            if x - 1 not in s: # starting sequence
                y = x
                while y in s: # but x in not in s
                    y += 1
                longest = max(longest, y - x)
        
        return longest