class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # reverse polish notation only applies to the last two elements in a stack
        stack = []
        for t in tokens:
            if t == "+":
                n = stack.pop() + stack.pop()
                stack.append(n)
            elif t == "-":
                a, b = stack.pop(), stack.pop() #ensures left num is on left hand side 
                n = b - a
                stack.append(n)
            elif t == "*":
                n = stack.pop() * stack.pop()
                stack.append(n)
            elif t == "/":
                a,b = stack.pop(), stack.pop()
                n = int(b / a)
                stack.append(n)
            else:
                stack.append(int(t))
        return stack[0] # return the first element, which is very likely the answer
