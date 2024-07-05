class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0

        rules_dict = {"type": 0, "color": 1, "name": 2}
        
        for item in items:
            rule = rules_dict[ruleKey]
            if ruleValue == item[rule]:
                count +=1

        return count