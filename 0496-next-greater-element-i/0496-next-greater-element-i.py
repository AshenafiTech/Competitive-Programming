class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    while (j < len(nums2)):
                        if nums2[j] > nums1[i]:
                            ans.append(nums2[j])
                            break
                        j=j+1
                    else:
                        ans.append(-1)
        return ans
        