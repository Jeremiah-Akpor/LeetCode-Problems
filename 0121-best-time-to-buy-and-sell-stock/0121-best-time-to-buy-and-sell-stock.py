class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        c_min = prices[0]
        c_profit = 0
        profit = 0
        for i in range(1, len(prices)):
            temp = c_min
            c_min = min(c_min, prices[i])
            c_profit = max(c_profit, prices[i] - c_min)
            if temp != c_min:
                c_profit = 0
            profit = max(c_profit, profit)
        return profit
