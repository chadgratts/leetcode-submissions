class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                current = num
                while current + 1 in nums:
                    current += 1
                longest = max(longest, current - num + 1)

        return longest