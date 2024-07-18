class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0
        r = len(numbers)-1
        res = []
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r-=1
            elif currSum < target:
                l+=1
            else:
                return [l+1, r+1]
            