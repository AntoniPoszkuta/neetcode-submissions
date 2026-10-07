class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if len(prices) < 2:
            return 0
        
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            if prices[r] - prices[l] > max_profit:
                max_profit = prices[r] - prices[l]
            r += 1

        return max(max_profit,0)