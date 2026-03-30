class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,1,5,6,7,1]
        #     1,      7
        # two pointers (buy and sell) at index 0 and 1
        # if buy < sell, update max_profit using max()
        # else increment both
        # always increment sell

        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return max_profit
