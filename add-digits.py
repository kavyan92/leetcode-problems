"""Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0"""

class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            new_num = 0
            for n in str(num):
                new_num += int(n)
                
            num = new_num
            
        return num

"""Runtime: 32 ms, faster than 72.26% of Python3 online submissions for Add Digits.
Memory Usage: 14.2 MB, less than 75.31% of Python3 online submissions for Add Digits."""