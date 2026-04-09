class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maximum = 0
        globmin = prices[0]
        
        for price in prices:
            if price < globmin:
                globmin = price 
            dif = price - globmin
            if dif > maximum:
                maximum = dif

        return maximum


