class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through nums array
        # iterate again, starting at the next number
        # if the two numbers add to target, return their indices

        for idx1 in range(len(nums)):
            for idx2 in range(idx1 + 1, len(nums)):
                if nums[idx1] + nums[idx2] == target:
                    return [idx1, idx2]
        
        