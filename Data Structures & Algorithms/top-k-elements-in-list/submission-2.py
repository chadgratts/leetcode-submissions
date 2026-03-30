class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        pairs = list(freq.items())
        pairs.sort(key=lambda pair: pair[1], reverse=True)

        return [pair[0] for pair in pairs[:k]]
