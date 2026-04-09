class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = []

        for i in range(len(nums)):
            mul = 1
            for index, num in enumerate(nums):
                if index == i:
                    continue
                else:
                    mul *= num
            d.append(mul)

        return d