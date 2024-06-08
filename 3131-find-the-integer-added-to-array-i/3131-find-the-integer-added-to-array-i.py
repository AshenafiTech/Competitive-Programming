class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        return nums2[0] - nums1[0]
        