class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i, num in enumerate(numbers):
            for index, number in enumerate(numbers):
                if num+number == target and i != index and i < index:
                    return [i+1, index+1]