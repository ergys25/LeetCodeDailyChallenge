# Given a string s, find the first non-repeating character in it and return
# its index. If it does not exist, return -1.

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)

        for st in (s):
            d[st] += 1

        for key in d.keys():
            if d[key] == 1:
                return s.find(key)
        return -1
