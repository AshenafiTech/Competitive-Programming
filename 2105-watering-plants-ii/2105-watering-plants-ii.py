class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l = 0
        r = len(plants)-1
        refill = 0
        A = capacityA
        B = capacityB
        while l < r:
            if capacityA < plants[l]:
                capacityA = A
                refill+=1
            if capacityB < plants[r]:
                capacityB = B
                refill+=1
            capacityA-=plants[l]
            capacityB-=plants[r]
            l+=1
            r-=1
        if l == r:
            if capacityA >= capacityB:
                if capacityA < plants[l]:
                    refill+=1
            else:
                if capacityB < plants[r]:
                    refill+=1
            

        return refill
