from collections import Counter

class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        count = Counter()
        
        # count each unique response per day
        for day in responses:
            for response in set(day):
                count[response] += 1
        
        # find the answer
        ans = ""
        max_freq = 0
        for response, freq in count.items():
            # choose higher freq, break tie by lexicographically smaller
            if freq > max_freq or (freq == max_freq and (ans == "" or response < ans)):
                max_freq = freq
                ans = response
        
        return ans
