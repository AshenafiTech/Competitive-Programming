class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        # Initialize an empty list to store the target array
        target = []
        
        for i in range(len(nums)):
            if index[i] == len(target):
                target.append(nums[i])
            else:
                target.insert(index[i], nums[i])

        return target