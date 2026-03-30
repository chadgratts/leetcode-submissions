class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for idx, num in enumerate(nums):
            if target - num in compliments:
                return [compliments[target - num], idx]
            else:
                compliments[num] = idx