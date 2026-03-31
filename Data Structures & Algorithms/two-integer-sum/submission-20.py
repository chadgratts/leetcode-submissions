class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # num: idx

        for idx, num in enumerate(nums):
            c = target - num
            if c in seen:
                return [seen[c], idx]
            seen[num] = idx
        return None