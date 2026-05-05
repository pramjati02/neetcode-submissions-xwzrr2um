class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        d = {}
        for i, num in enumerate(numbers):
            d[target-num] = i

        for i, num in enumerate(numbers):
            if num in d and i < d[num]:
                return [i+1, d[num]+1]