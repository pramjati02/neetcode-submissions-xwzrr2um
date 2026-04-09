class Solution:
    def findMin(self, nums: List[int]) -> int:
        rotation = len(nums)
        for i in range(len(nums)):
            if i+1 == len(nums):
                break
            if nums[i] > nums[i+1]:
                rotation = i+1
        
        left = len(nums) - rotation

        for i in range(left):
            popped = nums.pop()
            print(popped)
            nums.insert(0, popped)

        
        return nums[0]
        