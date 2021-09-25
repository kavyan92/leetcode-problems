"""You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.

Example 1:
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

Example 2:
Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match."""

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # create variable to count matching items
        matches = 0
        
        # loop through each item and check if the value matches the given key
        # if it does, increment counter by 1
        for item in items:
            if ruleKey == 'type' and item[0] == ruleValue:
                matches += 1
            if ruleKey == 'color' and item[1] == ruleValue:
                matches += 1
            if ruleKey == 'name' and item[2] == ruleValue:
                matches += 1
        
        # return variable keeping track of matches
        return matches

"""
Runtime: 236 ms, faster than 90.48% of Python3 online submissions for Count Items Matching a Rule.
Memory Usage: 20.4 MB, less than 88.96% of Python3 online submissions for Count Items Matching a Rule.
"""