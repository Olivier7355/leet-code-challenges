"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        temp =[]
        open1  = ['(','[','{']
        close1 = [')',']','}']
    
        temp.append(s[0])
        for char in range(1, len(s)) :
            #print(temp)
            
            if s[char] in open1 :
                temp.append(s[char])
                #print(temp)
            elif (temp) and (temp[-1] == open1[close1.index(s[char])]):
                del temp[-1]
                #print(temp)
            else :
                return False

        if not temp : return True
        else : return False
