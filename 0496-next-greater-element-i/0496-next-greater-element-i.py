class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict = {num:idx for idx, num in enumerate(nums1)}
        res = [-1]*len(nums1)

        for i in range(len(nums2)):
            if(nums2[i] not in nums1_dict):
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1_dict[nums2[i]]
                    res[idx] = nums2[j]
                    break

        return res
        