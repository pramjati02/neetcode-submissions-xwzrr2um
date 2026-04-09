class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        hs = {}

        for index, num in enumerate(nums):
            if index == 0:
                right = nums[index+1:len(nums)]
                hs[index] = right
                #print(hs)
            elif index == (len(nums)-1):
               left = nums[0:index]
               hs[index] = left
            else:
                right = nums[index+1:len(nums)]
                left = nums[0:index]
                hs[index] = left
                hs[index].extend(right)
        #print(hs.values())

        values = list(hs.values())
        
        ls = []
        
        for value in values:
            ls.extend(value)
        
        print(ls)

        product = 1
        output = []
        for i in range(0, len(ls)): 
            product *= ls[i]

            if (i+1)%(len(nums)-1) == 0:
                #print(product)
                print(i)
                output.append(product)
                product = 1
            
        return output


        """
        # PREVIOUS SOLUTION
        ls = []
        for index, num in enumerate(nums):
            product = 1
            for i in range(len(nums)):
                if i == index:
                    continue
                else:
                    product *= nums[i]
            ls.append(product)
            """