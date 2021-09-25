"""A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

Example 1:
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

Example 2:
Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
"""

class Solution:
    def sortSentence(self, s: str) -> str:
        # split sentence at spaces
        s = s.split()
        # create empty list to store new sentence
        original = []
        # create empty dict to store words with index value
        temp = {}
        # loop through words and identify last char in each string
        for word in s:
            i = word[-1]
            # slice last char off each string
            word = word[:-1]
            # add each item to dict
            temp[int(i)] = word
        
        # loop through dict items and add to empty list in sorted order
        for key, value in sorted(temp.items()):
            original.append(value)
        # return the new sentence as a string joined by spaces    
        return " ".join(original)

"""
Runtime: 32 ms, faster than 59.60% of Python3 online submissions for Sorting the Sentence.
Memory Usage: 14.1 MB, less than 74.99% of Python3 online submissions for Sorting the Sentence.
"""
        