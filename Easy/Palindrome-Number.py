"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]
    
print(isPalindrome(121))
