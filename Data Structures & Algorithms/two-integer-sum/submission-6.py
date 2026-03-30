class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a nested loop to find every pair time = O(n^2) space = O(1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # input: list of nums, integer
        # output: list of two integers (indices)

        # create hashmap (or do I call it a dict?)
        # iterate through nums with indices
        # if the compliment of current num is in the hashmap/dict, return current idx and idx of compliment
        
        compliments = {}

        for idx, num in enumerate(nums):
            if target - num in compliments:
                return [compliments[target-num], idx]

        # time: O(n)
        # space: O(n)
