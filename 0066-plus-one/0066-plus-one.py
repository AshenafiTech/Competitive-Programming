class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            # If the current digit is nine set it 0
            if digits[i] == 9:
                digits[i] = 0
            else:
                # If the current digits is not nine increment and return
                digits[i]+=1
                return digits

        # If all digits are 9, prepend 1 to the list
        return [1] + digits