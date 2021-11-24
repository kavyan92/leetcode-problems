"""Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        count = 0

        while count < n:
            s = s[1:] + s[0]
            count += 1
            if s == goal:
                return True

        return False

        # return len(s) == len(goal) and goal in s+s

"""Runtime: 43 ms, faster than 16.20% of Python3 online submissions for Rotate String.
Memory Usage: 14.2 MB, less than 47.37% of Python3 online submissions for Rotate String."""