class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        letters = []
        output = 0
        checked = []
        for letter in word:
            if letter.lower() not in checked and (letter.isupper() and letter.lower() in letters):
                output = output + 1
                checked.append(letter.lower())
            if letter not in checked and (letter.islower() and letter.upper() in letters):
                output = output + 1
                checked.append(letter)
            elif letter not in letters:
                letters.append(letter)
        print(letters)
        return output

        