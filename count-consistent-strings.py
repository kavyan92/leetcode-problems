"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # create counter variable
        counter = 0
        
        # loop through 'words' in list
        for word in words:
            # loop through characters in each word string
            for char in word:
                # if char is not in the allowed list, add to counter and break loop
                if char not in allowed:
                    counter += 1 
                    break
        # subtract counter variable from length of original list to get the number of consistent strings
        return len(words) - counter


"""Runtime: 276 ms, faster than 34.73% of Python3 online submissions for Count the Number of Consistent Strings.
Memory Usage: 16.3 MB, less than 28.16% of Python3 online submissions for Count the Number of Consistent Strings."""