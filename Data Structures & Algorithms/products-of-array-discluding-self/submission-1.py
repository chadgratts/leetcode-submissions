class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # iterate through the array
        # iterate once more
        # if the inner idx is not equal to the outer idx, add to product
        # back in the outer loop, append product to result array

        res = []

        for idx in range(len(nums)):
            product = 1
            for idx2 in range(len(nums)):
                if idx != idx2:
                    product *= nums[idx2]
            res.append(product)
        
        return res

