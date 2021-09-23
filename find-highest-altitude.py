"""There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0."""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # create list to keep track of incremental altitude.
        # first value will always be 0
        altitudes = [0]
        
        # loop through list of gains and add to most recent added altitude the list
        # keep appending that to 
        for value in gain:
            temp = altitudes[-1] + value
            altitudes.append(temp)
            
        # return the max of that list
        return max(altitudes)

"""
Runtime: 36 ms, faster than 68.24% of Python3 online submissions for Find the Highest Altitude.
Memory Usage: 14 MB, less than 87.37% of Python3 online submissions for Find the Highest Altitude.
"""