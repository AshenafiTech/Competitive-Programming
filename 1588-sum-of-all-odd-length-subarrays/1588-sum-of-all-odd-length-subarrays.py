class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        prefix = []
        curr = 0
        for i in arr:
            curr+=i
            prefix.append(curr)

        for i in range(len(arr)):
            res+=arr[i]
            for j in range(i+1, len(arr)):
                if (i+j) % 2 == 0:
                    res+=prefix[j]
                    if i > 0:
                        res-=prefix[i-1]

        return res