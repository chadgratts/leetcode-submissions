class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input array of integers
        # output array of integers
        # create the frequncies bucket (list)
        # create the frequencies dict
        # iterate through the nums list
        # populate frequencies dict
        # iterate through the keys of the frequencies dict
        
        bucket = [[] for _ in range(len(nums) + 1)]
        frequencies = {}
        res = []

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        for num, freq in frequencies.items():
            bucket[freq].append(num)
        
        for f in range(len(bucket) - 1, 0, -1):
            for num in bucket[f]:
                if len(res) == k:
                    return res
                res.append(num)
        return res