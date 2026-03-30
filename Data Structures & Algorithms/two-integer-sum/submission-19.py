class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for idx, num in enumerate(nums):
            c = target - num

            if c in compliments:
                return [compliments[c], idx]
            compliments[num] = idx