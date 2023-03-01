"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(strs: list[str]) -> str:
    commonPrefix=strs[0][0:1]
    counter = 0
    
    while (len(strs) > 1) and ("" not in strs) and (counter <= len(strs)+1) :
        commonPrefix = strs[0][0:1+counter]
        for i in range(0, len(strs)) :
            if not strs[i].startswith(commonPrefix) : return strs[0][0:1+counter-1]
        counter +=1
        print(commonPrefix)
    if len(strs) == 1 : return strs[0]
    elif "" in strs : return ""
    elif counter <= len(strs)+2 : return strs[0]
            
print(longestCommonPrefix(["flower","flower","flower","flower"]))
