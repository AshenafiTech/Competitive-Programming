class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        elements = set()

        for l , r in ranges:
            elements.update([num for num in range(l, r+1)])

        for num in range(left, right + 1):
            if num not in elements:
                return False

        return True