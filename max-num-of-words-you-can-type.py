"""There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

Example 1:
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.

Example 2:
Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

Example 3:
Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken."""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        count = len(text)
        for word in text:
            for letter in word:
                if letter in brokenLetters:
                    count -= 1
                    break
                
        return count

"""Runtime: 32 ms, faster than 72.36% of Python3 online submissions for Maximum Number of Words You Can Type.
Memory Usage: 14.4 MB, less than 31.53% of Python3 online submissions for Maximum Number of Words You Can Type."""