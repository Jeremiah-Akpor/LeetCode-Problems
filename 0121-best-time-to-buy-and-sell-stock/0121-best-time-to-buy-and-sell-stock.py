class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
            You are given an array prices where prices[i]
            is the price of a given stock on the ith day.
            You want to maximize your profit by choosing a
            single day to buy one stock and choosing a
            different day in the future to sell that stock.
        Args:
            prices (list[int]): natural number

        Returns:
            int: Return the maximum profit you can
            achieve from this transaction. If you cannot
            achieve any profit, return 0
        """
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
