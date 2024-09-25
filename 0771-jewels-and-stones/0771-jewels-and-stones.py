class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewels_count = {}

        for stone in stones:
            if stone in jewels:
                if stone in jewels_count:
                    jewels_count[stone]+=1
                else:
                    jewels_count[stone] = 1
        
        count = 0
        for i in jewels_count.values():
            count+=i

        return count