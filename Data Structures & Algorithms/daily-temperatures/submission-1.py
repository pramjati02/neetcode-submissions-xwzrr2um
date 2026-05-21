class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # where we put our differences 
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # pop any pairs in the stack that are lower than the current pair (hence "while")
                stackT, stackInd = stack.pop() # pop the pair 
                res[stackInd] = i - stackInd # input difference to respective temperature indicie in results
            stack.append((t, i)) # append the pair to stack 
        return res