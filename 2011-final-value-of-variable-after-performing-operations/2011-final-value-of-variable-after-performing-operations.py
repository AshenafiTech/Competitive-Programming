class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        
        for o in operations:
            if (o=="X++" or o=="++X"):
                x+=1
            elif (o=="--X" or o=="X--"):
                x-=1

            print(x)
        return x