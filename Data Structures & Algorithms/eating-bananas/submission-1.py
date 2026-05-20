class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = math.floor((low+high)/2)
            total_hours = 0
            for p in piles:
                # we do not start on a new pile until the next FULL hour 
                # eg. if we finish a pile in 2.5 hours, we sit idle for the remaining 0.5 hours
                # hence that pile will take a total of 3 hours
                # therefore we round up to nearest whole number using math.ceil, 
                # ensuring hours are always be integers
                hours = math.ceil(p/mid) 
                total_hours += hours
            if total_hours <= h:
                k = mid
                high = mid-1
                # if total_hours is less than h
                # we might want to explore lower values
                # to see if we can find a lower number of total_hours
            else:
                low = mid+1
                print(total_hours, mid)
                # otherwise, we increase our threshold to increase eating rate
                # to find a suitable number of hours
            

        return k
                