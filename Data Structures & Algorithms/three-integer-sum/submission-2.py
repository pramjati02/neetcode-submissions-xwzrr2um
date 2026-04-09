class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}

        for index, num in enumerate(nums):
            for i in range(len(nums)):
                if index >= i:
                    continue
                else:
                    d[(index, i)] = 0-(num+nums[i])
        print(d)

        lindex = []
        for index, num in enumerate(nums):
            for key, value in d.items():
                if num == value and not index in list(key):
                    ilist = list(key)
                    ilist.append(index)
                    lindex.append(ilist)
        
        print(lindex)
        
        triple = []
        for i in lindex:
            l = []
            first = nums[i[0]] 
            l.append(first)
            second = nums[i[1]] 
            l.append(second)
            third = nums[i[2]] 
            l.append(third)
            l.sort()
            if l in triple:
                continue
            else:
                triple.append(l)
    
            
        
        return triple