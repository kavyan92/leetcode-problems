"""Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b"."""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        
        for char in s:
            if char == '#' and len(s_stack) > 0:
                s_stack.pop()
            elif char == '#' and len(s_stack) == 0:
                continue
            else:
                s_stack.append(char)
    
        for char in t:
            if char == '#' and len(t_stack) > 0:
                t_stack.pop()
            elif char == '#' and len(t_stack) == 0:
                continue
            else:
                t_stack.append(char)

        return s_stack == t_stack
                
                