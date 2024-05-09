class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0
        for operator in operations:
            if operator == "--X" or operator == "X--":
                res=res-1
            elif operator == "X++" or operator == "++X":
                res=res+1
        return res
        