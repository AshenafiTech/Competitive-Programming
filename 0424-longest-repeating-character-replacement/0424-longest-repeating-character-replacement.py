class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        freq = [0]*26
        max_f = 0
        for r in range(len(s)):
            right_char = ord(s[r]) - ord('A')
            freq[right_char]+=1
            max_f = max(max_f, freq[right_char])
            
            if (r-l+1) - max_f > k:
                left_char = ord(s[l]) - ord('A')
                freq[left_char]-=1
                l+=1

            max_len = max(max_len, r-l+1)


        return max_len 
