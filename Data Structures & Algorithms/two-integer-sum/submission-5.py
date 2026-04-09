class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # have to return two indexes that add up to the target
        d = {}

        # for each number, calculate difference between target and insert index as its value
        for index, num in enumerate(nums):
            d[target-num] = index

        # iterate through nums again
        # for each num, find if it exists in the keys and if the indexes are not the same
        for i, num in enumerate(nums):
            if num in d and d[num] != i:
                return [min(i, d[num]), max(i, d[num])] 