class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input: array of integers -> daily stock prices
        # output: int -> max profit from one buy and one later sell

        # results:
        # O(n) time -> moves across the whole array of prices
        # O(1) space -> uses a constant number of variables

        left = 0
        right = left + 1
        current_profit = 0

        # prevents out of bounds
        while right < len(prices):
            # if sell is less than buy -> move left to right
            if prices[right] < prices[left]:
                left = right
            # if sell is greater than buy -> calculate profit
            if prices[right] > prices[left]:
                # check if profit is less than new potential profit
                if current_profit < (prices[right] - prices[left]):
                    current_profit = prices[right] - prices[left]
        
            # only move right
            right += 1
        return current_profit
            