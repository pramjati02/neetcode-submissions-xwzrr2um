class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        nums.sort()
        print(nums)

        #counts = []
        max_count = 0
        count = 1
        for index, num in enumerate(nums):
            if count > max_count:
                max_count = count 

            if index+1 > len(nums)-1:
                break
            
            if nums[index+1] - num == 1:
                count += 1
                print(count)
            elif nums[index+1] - num == 0:
                continue
            else:
                #counts.append(count)
                count=1

        #print(counts)

        return max_count

        """
        s = set(nums)
        print(nums)
        a = []
        for num in s:
            if num+1 in s and num in a and num+1 in a:
                continue
            elif num+1 in s and not num in a and not num+1 in a:
                a.insert
        """