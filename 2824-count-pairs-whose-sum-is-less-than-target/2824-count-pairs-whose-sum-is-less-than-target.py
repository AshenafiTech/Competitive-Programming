class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, 1
        pair_count = 0
        
        while i < len(nums) - 1:
            if nums[i] + nums[j] < target:
                pair_count+=1
            j+=1
            
            if j==len(nums):
                i+=1
                j=i+1
        return pair_count