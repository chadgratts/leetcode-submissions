class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # { number: its index }

        # iterate through nums array
        # check a dict to see if another number can be used to make sum
            # subtract the current number from the target. if that num is in the dict, return indices
        # if not, add the current num to dict

        seen = {}

        for i, num in enumerate(nums):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            else:
                seen[nums[i]] = i