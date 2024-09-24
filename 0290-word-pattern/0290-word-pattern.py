class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        d = {}
        re_d = {}

        if len(pattern) != len(s_list):
            return False

        for i in range(len(pattern)):
            p_char = pattern[i]
            word = s_list[i]
            if p_char not in d:
                d[p_char] = word
            else:
                if d[p_char] != word:
                    return False

            if word not in re_d:
                re_d[word] = p_char
            else:
                if re_d[word] != p_char:
                    return False 

        return True