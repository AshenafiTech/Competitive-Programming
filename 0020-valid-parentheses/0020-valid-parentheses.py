class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paired = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in paired.keys():
                stack.append(char)
            elif stack:
                last = stack[-1]
                if paired[last] == char:
                    stack.pop()
                else:
                    return False
            else: return False

        return not stack

        