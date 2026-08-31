class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer
        # left and right pointers; right pointer starts +1
        # compare the two pointers
        # if left is greater than right -> loss
        # else -> move the pointers by one

        
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if (prices[right] > prices[left]):
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            else:
                left = right
            right += 1

        if max_profit < 1:
            return 0
        else:
            return max_profit