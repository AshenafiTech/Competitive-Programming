class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        store = {"*", "/", "+", "-"}
        
        for token in tokens:
            if token not in store:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    if (a<0 and b>0) or (a>0 and b<0):
                        ans = abs(a)//abs(b)
                        stack.append(-ans)
                    else:
                        stack.append(a//b)
        return stack.pop()