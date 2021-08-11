"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        new_s = []
        for word in s:
            word = word[::-1]
            new_s.append(word)
        
        return " ".join(new_s)

# Runtime: 28 ms, faster than 92.16% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.9 MB, less than 45.09% of Python3 online submissions for Reverse Words in a String III.