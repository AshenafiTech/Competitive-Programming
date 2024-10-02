class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        N = len(nums)
    
        for i in range(N):
            low, high = i+1, N-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while low < high:
                sm = nums[i] + nums[low] + nums[high]

                if sm == 0:
                    triplets.append([nums[i], nums[low], nums[high]])
                    low-=1
                    high-=1

                    while low < high and nums[low] == nums[low-1]:
                        low+=1
                    while low < high and nums[high] == nums[high+1]:
                        high-=1
                elif sm < 0:
                    low+=1
                elif sm > 0:
                    high-=1
                    
        return triplets