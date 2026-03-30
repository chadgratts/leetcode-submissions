class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # turn the input array into a set
        # return an equality expression between this set and the input array

        return len(set(nums)) != len(nums)