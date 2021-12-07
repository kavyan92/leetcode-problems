"""You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array. Return the sum of all the unique elements of nums.

Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15."""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
            
        uniques = []
        
        for k, v in count_dict.items():
            if v == 1:
                uniques.append(k)
                
        return sum(uniques)

"""Runtime: 36 ms, faster than 60.56% of Python3 online submissions for Sum of Unique Elements.
Memory Usage: 14.1 MB, less than 75.07% of Python3 online submissions for Sum of Unique Elements."""