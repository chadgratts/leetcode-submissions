class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # call a function that removes duplicates
        seen = []
        for num in nums:
            if num in seen:
                return True
            seen.append(num)
        
        return False