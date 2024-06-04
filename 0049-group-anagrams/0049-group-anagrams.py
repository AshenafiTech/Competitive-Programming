class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = defaultdict(list)
        
        for strg in strs:
            sorted_str = ''.join(sorted(strg))
            output[sorted_str].append(strg)
        
        return list(output.values())


            