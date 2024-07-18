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
            if numbers[l] + numbers[r] > target:
                r-=1
                continue
            if numbers[l] + numbers[r] < target:
                l+=1
                continue
            if numbers[l] + numbers[r] == target:
                res.append(l+1)
                res.append(r+1)
                break
                
        return res
            