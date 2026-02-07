class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {name: i for i, name in enumerate(list1)}
        min_sum = float('inf')
        result = []
        for j, name in enumerate(list2):
            if name in index_map:
                s = j + index_map[name]
                if s < min_sum:
                    min_sum = s
                    result = [name]

                elif s == min_sum:
                    result.append(name)

        return result




