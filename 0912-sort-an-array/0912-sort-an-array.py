class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left_half = merge_sort(nums[:mid])
            right_half = merge_sort(nums[mid:])

            return merge(left_half, right_half)

        def merge(left, right):
            i = j = 0
            sorted_array = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_array.append(left[i])
                    i+=1
                else:
                    sorted_array.append(right[j])
                    j+=1

            sorted_array.extend(left[i:])
            sorted_array.extend(right[j:])

            return sorted_array
        return merge_sort(nums)