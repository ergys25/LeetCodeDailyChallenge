"""
2405
Given a string s, partition the string into one or more substrings such that the characters 
in each substring are unique. That is, no letter appears in a single substring more than once.
Return the minimum number of substrings in such a partition.
Note that each character should belong to exactly one substring in a partition.
"""

class Solution:
    def partitionString(self, s: str) -> int:
        i, ans, flag = 0, 1, 0
        while i < len(s):
            val = ord(s[i]) - ord('a')
            if flag & (1 << val):
                flag = 0
                ans += 1
            flag |= 1 << val
            i += 1
        return ans
