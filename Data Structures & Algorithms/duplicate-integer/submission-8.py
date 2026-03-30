class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate through the list, keeping a count in a dict
        count = {}

        for num in nums:
            if num in count:
                return True
            else:
                count[num] = 1
        return False