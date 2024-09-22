class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = count = 0
        i = 0
        while i < len(nums):
            j = i
            if nums[i] == 1:
                while j < len(nums) and nums[j] == 1:
                    count+=1
                    j+=1
                else:
                    m = max(count, m)
                    count = 0
            i = j+1

        return m