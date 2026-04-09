class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for index, num in enumerate(nums):
                if nums[i] == num and index != i:
                    return True
        return False