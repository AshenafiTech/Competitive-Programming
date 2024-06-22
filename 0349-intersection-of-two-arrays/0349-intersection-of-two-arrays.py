class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mydict = {}

        for num in nums1:
            if (num in nums2) and (num not in mydict.keys()):
                mydict[num] = num
        return list(mydict.keys())