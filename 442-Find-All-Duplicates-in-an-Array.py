class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        result = []
        for key, value in d.items():
            if value == 2:
                result.append(key)

        return result