class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0
        for operator in operations:
            if "-" in operator:
                res=res-1
            elif "+" in operator:
                res=res+1
        return res
        