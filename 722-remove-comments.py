class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        buffer = []
        inBlock = False


        for line in source:
            i = 0
            while i < len(line):
                if inBlock:
                    if i + 1 < len(line) and line[i:i+2] == "*/":
                        inBlock = False
                        i+=2
                    else:
                        i+=1
                else:
                    if i+1 < len(line) and line[i:i+2] == "//":
                        break
                    elif i+1 < len(line) and line[i:i+2] == "/*":
                        inBlock = True
                        i+=2
                    else:
                        buffer.append(line[i])
                        i+=1

            if not inBlock and buffer:
                ans.append("".join(buffer)) 
                buffer.clear()

        return ans