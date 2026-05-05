class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        d = {}

        for i, num in enumerate(numbers):
            tmp = target-num
            if tmp in d:
                return [d[tmp]+1, i+1]
            d[num] = i
        return []