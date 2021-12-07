"""Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]"""

from itertools import repeat
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = []
        letters = {}
        first = words[0]
        for char in first:
            letters[char] = letters.get(char, 0) + 1
            
        for k, v in letters.items():
            for word in words[1:]:
                if k not in word:
                    letters[k] = 0
                    break
                else:
                    if v > word.count(k):
                        v = word.count(k)
                        letters[k] = v
        
        for k, v in letters.items():
            if v > 0:
                common.extend(repeat(k, v))
            
        return common
            
"""Runtime: 40 ms, faster than 95.47% of Python3 online submissions for Find Common Characters.
Memory Usage: 14.3 MB, less than 84.41% of Python3 online submissions for Find Common Characters."""