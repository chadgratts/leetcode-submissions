class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        res = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if sum([nums[i], nums[j], nums[k]]) == 0:
                        sorted_nums = tuple(sorted([nums[i], nums[j], nums[k]]))

                        if sorted_nums not in seen:
                            seen.add(sorted_nums)
                            res.append(list(sorted_nums))
        
        return res