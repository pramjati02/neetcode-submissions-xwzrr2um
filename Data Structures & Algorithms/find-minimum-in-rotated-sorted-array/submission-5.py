class Solution:
    def findMin(self, nums: List[int]) -> int:
        rotation = 0
        for i in range(len(nums)):
            if i+1 == len(nums):
                break
                
            if nums[i] > nums[i+1]:
                rotation = i+1
                break



        return nums[rotation]
        