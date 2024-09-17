class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        mn = len(strs[0])

        for st in strs:
            mn = min(mn, len(st))

        res = ""
        for i in range(mn):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return res   
            res+=strs[0][i]

        return res