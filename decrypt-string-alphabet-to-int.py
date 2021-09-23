"""Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        # create list containing all lowercase letters
        alphabet = '0abcdefghijklmnopqrstuvwxyz'
        # create empty list to store each decrypted value
        decrypted = []
        # make s into a list for the loop
        s = list(s)
        # run through while loop until length of list is 0
        while len(s) > 0:
            # create temp variable to store value of last char in s
            temp = s.pop(-1)
            # if var is # then take the last two chars of s 
            if temp == '#':
                x = s.pop(-2)
                y = s.pop(-1)
                z = str(x) + str(y)
                # index into alphabet to find decrypted value and add to empty list
                decrypted.append(alphabet[int(z)])
            else:
                # if not # then index into alphabet with temp to find decrypted value and add to empty list
                decrypted.append(alphabet[int(temp)])
        # join new list and reverse it
        decrypted = ''.join(reversed(decrypted))
        # return string
        return decrypted

"""Runtime: 62 ms, faster than 5.28% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
Memory Usage: 14.1 MB, less than 77.95% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping."""