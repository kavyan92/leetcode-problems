"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome."""

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()

        s_reverse = ''
        n = len(s)

        # for i in range(n - 1, -1, -1):
        #     s_reverse += s[i]
        # print(s_reverse)

        # if s == s_reverse:
        #     return True
        if s == s[::-1]:
            return True

        return False

"""Runtime: 48 ms, faster than 67.49% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15.7 MB, less than 22.26% of Python3 online submissions for Valid Palindrome."""