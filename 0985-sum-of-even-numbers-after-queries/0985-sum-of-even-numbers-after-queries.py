class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(x for x in nums if x % 2 == 0)
        result = []

        for val, idx in queries:
            
            # if current value is even, remove from sum
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]

            # update value
            nums[idx] += val

            # if new value is even, add to sum
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            result.append(even_sum)

        return result
