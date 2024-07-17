class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res = 0
        currSum = sum(arr[:k-1])
        
        for l in range(len(arr) - k + 1):
            currSum += arr[l+k-1]
            if(currSum/k) >= threshold:
                res+=1
            currSum-=arr[l]
            
        return res