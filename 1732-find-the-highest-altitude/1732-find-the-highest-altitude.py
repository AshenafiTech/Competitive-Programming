class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes = [0]
        for i in range(len(gain)):
            altitudes.append(altitudes[i]+gain[i])
        
        largest = 0
        for i in range(len(altitudes)):
            if altitudes[i] > largest:
                largest = altitudes[i]
        
        return largest
        