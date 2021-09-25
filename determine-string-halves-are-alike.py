"""You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

Example 3:
Input: s = "MerryChristmas"
Output: false

Example 4:
Input: s = "AbCdEfGh"
Output: true"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        #create a set of uppercase and lowercase vowels. 
        #sets have faster lookup time
        vowels = set('aeiouAEIOU')
        
        #slice string in half at midpoint
        a = s[int(len(s)/2):]
        b = s[:int(len(s)/2)]
        
        #initiate variables to keep track of number of vowels in each half
        a_vowels = 0
        b_vowels = 0
        #loop through each half and check how many vowels are in each
        for char in a:
            if char in vowels:
                a_vowels += 1
        
        for char in b:
            if char in vowels:
                b_vowels += 1

        # if a_vowels and b_vowels are equal, return True
        
        if a_vowels == b_vowels:
            return True

"""
Runtime: 28 ms, faster than 95.66% of Python3 online submissions for Determine if String Halves Are Alike.
Memory Usage: 14.4 MB, less than 31.91% of Python3 online submissions for Determine if String Halves Are Alike.
"""