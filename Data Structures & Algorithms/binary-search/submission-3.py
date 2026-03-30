class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # while left is not equal to right index pointer
        # select the mid index of the list
        # if the number at mid_index is less than target, point to index 0 and 1 - mid_index
        # else point to mid_index + 1 and last index
        # if the number at mid_index equals target, return mid_index
        # implicitly return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2
            print(mid_index)
            if nums[mid_index] < target:
                left = mid_index + 1
            elif nums[mid_index] > target:
                right = mid_index - 1
            else:
                return mid_index
        
        return -1