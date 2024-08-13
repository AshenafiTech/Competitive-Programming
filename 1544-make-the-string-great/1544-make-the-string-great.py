class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if stack:
                top = stack[-1]
                if s[i].lower() == top.lower() and s[i] != top:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        return ''.join(stack)