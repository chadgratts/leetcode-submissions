class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # turn the nums array into a tuple
        # iterate through it
        # check the frequency of each number in nums
        # populate a dictionary with the keys as numbers and values as freqs
        # create an array of keys (nums)
        # sort this array from large to small
        # slice this array with k and return it

        unique_nums = set(nums)
        dic = {}

        for num in unique_nums:
            freq = nums.count(num)

            if num not in dic:
                dic[num] = freq
        
        print(unique_nums)
        print(sorted(unique_nums, key=lambda num: dic[num]))
        return sorted(unique_nums, key=lambda num: dic[num])[-k:]