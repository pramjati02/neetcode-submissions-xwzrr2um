class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        for i1, h1 in enumerate(heights):
            #length = 1
            for i2, h2 in enumerate(heights):
                if i1==i2:
                    continue
                else:
                    area = abs(i2-i1)*min(h1, h2)
                    #print(f"i1: {i1}, i2: {i2}, h1: {h1}, h2: {h2}, area: {area}")
                    areas.append(area)

        return max(areas)

        """
        #diflist = []
        mindif = 0
        for index, h in enumerate(heights):
            dif = maximum-h
            if index == 0:
                mindif = dif
                mini = index
            else:
                if dif <= mindif:
                    mindif = dif 
                    mini = index
                else:
                    continue 
        
        max2 = heights[mini]
        
        #print("final max:", maximum)
        #print(max2)

        most = maximum + max2

        return most
        """
