class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = []
        s = set(nums)
    
        for num in s:
            f = nums.count(num)
            freq.append([f, num])
        
        print(freq)
        freq.sort()
        
        print(freq)

        l = []
        for f in freq:
            l.append(f[1])

        return l[-k:]