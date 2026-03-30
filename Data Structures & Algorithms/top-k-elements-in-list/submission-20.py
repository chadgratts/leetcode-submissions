class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        groups = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, freq in freq.items():
            groups[freq].append(num)
        
        for i in range(len(groups) - 1, 0, -1):
            for num in groups[i]:
                res.append(num)
                if len(res) == k:
                    return res