"""A string is good if there are no repeated characters.Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

Example 2:
Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc"."""

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # if length of string is less than 3, there are no 'good substrings'
        if len(s) < 3:
            return 0
        # if length of string is at least 3
        if len(s) >= 3:
            # set variables to keep track of indexes as you move through string
            # initialize counter variable
            left, right, count = 0, 3, 0
            
            # loop through string until right index variable equals length of string
            while right <= len(s):
                # temp variable to store current substring
                temp = s[left:right]
                # if the length of the set of the substring is equal to the length of the substring(3), all chars are unique. increment counter
                if len(set(temp)) == len(temp):
                    count += 1
                # increment index variables
                left += 1
                right +=1
        
        # return counter
        return count
            
"""Runtime: 28 ms, faster than 92.58% of Python3 online submissions for Substrings of Size Three with Distinct Characters.
Memory Usage: 14.2 MB, less than 47.16% of Python3 online submissions for Substrings of Size Three with Distinct Characters."""