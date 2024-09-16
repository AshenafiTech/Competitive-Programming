class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        
        for num in nums:
            if abs(num) < abs(closest):
                closest = num
            if abs(closest) == num:
                closest = num

        return closest

            