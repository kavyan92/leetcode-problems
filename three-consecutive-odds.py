"""Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 
Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds."""

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        
        for i in range(0, n-2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
                
        return False


"""Runtime: 64 ms, faster than 21.02% of Python3 online submissions for Three Consecutive Odds.
Memory Usage: 14.3 MB, less than 84.28% of Python3 online submissions for Three Consecutive Odds."""