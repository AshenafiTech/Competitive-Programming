from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            new_dict[sorted_s].append(s)

        for s in new_dict.values():
            result.append(s)

        return result
    