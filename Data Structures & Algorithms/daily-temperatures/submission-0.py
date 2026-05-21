class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    dif = j-i
                    result.append(dif)
                    break
                elif j == len(temperatures)-1 and temperatures[j] <= temperatures[i]:
                    result.append(0)
        
        return result