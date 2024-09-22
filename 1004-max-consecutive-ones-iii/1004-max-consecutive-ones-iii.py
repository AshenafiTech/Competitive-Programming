class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w = 0
        n = len(nums)
        l = 0
        zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros+=1

            while zeros > k:
                if nums[l] == 0:
                    zeros-=1
                l+=1
            w = i-l+1
            max_w = max(w, max_w)

        return max_w 
        
        
