"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, char in enumerate(s):
            if s.count(char) == 1:
                return i
        
        return -1

"""Runtime: 4940 ms, faster than 5.11% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.3 MB, less than 89.32% of Python3 online submissions for First Unique Character in a String."""