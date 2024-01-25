from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):

            if p1 == len(text1) or p2 == len(text2):
                return 0
            option_1 = memo_solve(p1+1, p2)
            first_occurence = text2.find(text1[p1], p2)
            option_2 = 0
            if first_occurence != -1:
                option_2 = 1+memo_solve(p1+1, first_occurence+1)
            return max(option_1, option_2)
        return memo_solve(0, 0)
