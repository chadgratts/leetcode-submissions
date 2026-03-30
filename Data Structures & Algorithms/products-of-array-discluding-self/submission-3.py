class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        l_product = 1
        r_product = 1

        for num in nums:
            result.append(l_product)
            l_product *= num
        
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= r_product
            r_product *= nums[i]

        return result