class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i1, price in enumerate(prices):
            for i2 in range(i1+1, len(prices)):
                rev = prices[i2] - price
                if rev >= 1:
                    profits.append(rev)
                else:
                    continue

        if len(profits) > 0:
            return max(profits)
        return 0
