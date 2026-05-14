class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1

        while first <= last:
            
            n = math.floor((first+last)/2)
            print(n)

            if target > nums[n]:
                first = n+1
            elif target < nums[n]:
                last = n-1
            else:
                return n
        return -1
            

            