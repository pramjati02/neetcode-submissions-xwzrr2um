class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        ls = []
        for key,value in d.items():
            ls.append([value,key])
        ls.sort()
        
        ls = ls[len(ls)-k:len(ls)]

        new_ls = []
        for i in range(len(ls)):
            new_ls.append(ls[i][1])

        return new_ls
            
            
