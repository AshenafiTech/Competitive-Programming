class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_sorted = sorted(nums1)
        nums2_sorted = sorted(nums2)
        intersection = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1_sorted[i] == nums2_sorted[j]:
                intersection.append(nums1_sorted[i])
                i+=1
                j+=1
            elif nums1_sorted[i] < nums2_sorted[j]:
                i+=1
            else:
                j+=1
        return intersection