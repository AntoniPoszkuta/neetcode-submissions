class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for buy in range(len(prices)-1):
            for sell in range(buy, len(prices)):
                max_profit =  max(prices[sell] - prices[buy], max_profit)
        
        return max_profit
        