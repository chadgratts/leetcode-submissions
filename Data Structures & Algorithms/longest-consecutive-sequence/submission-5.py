class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sorted_nums = sorted(nums)
        max_streak = 0
        current_streak = 1

        for i in range(1, len(nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                continue
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 1
        
        max_streak = max(max_streak, current_streak)
        return max_streak
