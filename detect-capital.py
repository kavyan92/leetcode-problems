"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # account for no string or one lettered string
        if len(word) <= 1:
            return True
        # pull first element of string and if it is uppercase
        if word[0].isupper():
            # if the rest of the string is upper, its valid
            if word[1:].isupper():
                return True
            # if the rest of the string is lower, its valid
            if word[1:].islower():
                return True
        # if first element of string is lower
        if word[0].islower():
            # rest of string must be lower
            if word[1:].islower():
                return True
        
        else:
            return False


# Runtime: 20 ms, faster than 98.77% of Python3 online submissions for Detect Capital.
# Memory Usage: 14.3 MB, less than 46.09% of Python3 online submissions for Detect Capital.