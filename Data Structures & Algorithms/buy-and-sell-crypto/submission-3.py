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


