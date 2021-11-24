"""Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        s = set(nums)
        for i in range(1, n + 1):
            if i not in s:
                ans.append(i)
                
        return ans
                
"""Runtime: 332 ms, faster than 84.72% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 24.4 MB, less than 32.20% of Python3 online submissions for Find All Numbers Disappeared in an Array."""