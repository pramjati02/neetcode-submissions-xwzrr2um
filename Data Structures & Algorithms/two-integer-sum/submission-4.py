class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for index, num in enumerate(nums):
            d[target-num] = index

        for i, num in enumerate(nums):
            if num in d and d[num] != i:
                return [min(i, d[num]), max(i, d[num])] 