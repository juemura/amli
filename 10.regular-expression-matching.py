#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (24.99%)
# Total Accepted:    278.8K
# Total Submissions: 1.1M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
# 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
# it matches "aab".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
# 
# 
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_size = len(s)
        p_size = len(p)
        # Check edge cases
        if p_size == 0:
            return s_size == 0
        if p_size == 1:
            return s_size == 1 and (p == s or p == '.')
        if s_size == 0:
            for i in range(1, p_size, 2):
                if p[i] != '*':
                    return False
            return p_size % 2 == 0

        # Create table
        d = [[False]*(s_size+1) for _ in range(p_size+1)]

        # Define values for first row and column
        d[0][0] = True
        for i in range(1, p_size, 2):
            d[i+1][0] = p[i] == '*' and d[i-1][0]

        # Tabulation
        for i in range(p_size):
            for j in range(s_size):
                if p[i] == s[j] or p[i] == '.':
                    d[i+1][j+1] = d[i][j]
                elif p[i] == '*':
                    if p[i-1] == '.' and d[i+1][j]:
                        d[i+1][j+1] = True
                    elif p[i-1] == s[j]:
                        d[i+1][j+1] = (d[i-1][j+1] or d[i][j+1] or d[i][j])
                    else:
                        d[i+1][j+1] = d[i-1][j+1]
                else:
                    d[i+1][j+1] = False
        return d[p_size][s_size]
        

