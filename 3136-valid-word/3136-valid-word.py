class Solution:
    def isValid(self, word: str) -> bool:
        lst = ["a", "e", "i", "o", "u"]
        cons = False
        vowel = False
        if len(word) < 3:
            return False
        for ch in word:
            if not ch.isalnum():
                return False
            else:
                if ch.lower() in lst:
                    vowel = True
                    continue
                elif ch.isalpha():
                    cons = True
        return cons and vowel