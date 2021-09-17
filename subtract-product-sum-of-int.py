"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
"""

# set two new variables to keep track of product and sum
    product = 1
    add = 0
    
    # loop through each char in number and update variables accordingly
    for char in str(n):
        product = product * int(char)
        add += int(char)
        
    # return product minus sum
    return product - add


"""
Runtime: 28 ms, faster than 83.24% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 14.1 MB, less than 69.53% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
"""