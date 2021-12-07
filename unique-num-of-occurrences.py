"""Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = {}
        for val in arr:
            count_dict[val] = count_dict.get(val, 0) + 1
        
        v = list(count_dict.values())
        for val in v:
            if v.count(val) > 1:
                return False
            
        return True

"""Runtime: 36 ms, faster than 70.68% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 14.4 MB, less than 64.74% of Python3 online submissions for Unique Number of Occurrences."""