class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = math.floor((low+high)/2)
            total_hours = 0
            for p in piles:
                hours = math.ceil(p/mid) # round up to nearest whole number
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
                