"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_set = set(t)

        if set(s) != t_set:
            return False 

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t_set:
            if char not in s_dict.keys() or t.count(char) != s_dict[char]:
                return False

        return True

"""Runtime: 62 ms, faster than 28.35% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.6 MB, less than 57.14% of Python3 online submissions for Valid Anagram."""