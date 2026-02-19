class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        if len(changed) % 2 != 0:
            return []

        count = Counter(changed)
        original = []

        for x in sorted(count.keys()):
            if x == 0:
                if count[0] % 2 != 0:
                    return []  # cannot pair all zeros
                original.extend([0] * (count[0] // 2))
            else:
                if count[x] > count[2*x]:
                    return []  # cannot pair x with 2*x
                original.extend([x] * count[x])
                count[2*x] -= count[x]

        return original
