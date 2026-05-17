class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freqs.items():
            buckets[count].append(num)
        
        res = []

        for b in range(len(buckets) - 1, 0, -1):
            for num in buckets[b]:
                res.append(num)
                if len(res) == k:
                    return res