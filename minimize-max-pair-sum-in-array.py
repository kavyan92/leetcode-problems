"""The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.

Example 1:
Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

Example 2:
Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8."""

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # create empty list to store sum of pairs
        sums = []
        # sort the list of nums and get the length
        nums.sort()
        n = len(nums)
        
        # initialize two variables
        left = 0
        right = n - 1
        # loop through list from the start and the end and create pairs between largest and smallest value
        # increment variales as you go
        while left < right:
            a = nums[left]
            b = nums[right]
            sums.append(a + b)
            left += 1
            right -= 1

        # return max of sums
        return max(sums)

"""Runtime: 1160 ms, faster than 79.37% of Python3 online submissions for Minimize Maximum Pair Sum in Array.
Memory Usage: 28 MB, less than 48.22% of Python3 online submissions for Minimize Maximum Pair Sum in Array."""
            
        
        

