class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        res = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    triplet = (nums[i], nums[j], nums[k])
                    if triplet not in seen:
                        seen.add(triplet)
                        res.append(list(triplet))
                    j += 1
                    k -= 1
        return res