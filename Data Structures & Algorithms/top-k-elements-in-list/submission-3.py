class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = []
        s = set(nums)
    
        for num in s:
            f = nums.count(num)
            freq.append([f, num])
        
        freq.sort() # sorts by the first value in each sublist (f)

        l = []
        for f in freq:
            l.append(f[1])

        return l[-k:]