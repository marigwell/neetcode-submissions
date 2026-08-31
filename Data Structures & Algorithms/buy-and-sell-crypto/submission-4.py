class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input: array of integers -> daily stock prices
        # output: int -> max profit from one buy and one later sell

        left = 0
        right = left + 1
        current_profit = 0

        while left < len(prices) and right < len(prices):
            if prices[right] < prices[left]:
                left = right
            if prices[right] > prices[left]:
                if current_profit < (prices[right] - prices[left]):
                    current_profit = prices[right] - prices[left]
        
            right += 1
        return current_profit
            