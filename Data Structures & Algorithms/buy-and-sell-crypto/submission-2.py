class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maximum = 0
        for index, price in enumerate(prices):
            if index == 0:
                globmin = price
            if price < globmin:
                globmin = price 
            dif = price - globmin
            if dif > maximum:
                maximum = dif

        return maximum
        """
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
"""

