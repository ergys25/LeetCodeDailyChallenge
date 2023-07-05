"""
1639
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.
"""


class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        mod = 10**9 + 7
        m, n = len(words), len(words[0])
        
        # frequency array for each character in each column
        freq = [[0] * 26 for _ in range(n)]
        for j in range(n):
            for i in range(m):
                freq[j][ord(words[i][j]) - ord('a')] += 1
        
        # dp array to store the number of ways to form the prefix of target
        dp = [1] + [0] * len(target)
        
        # fill dp array from left to right
        for j in range(n):
            for i in range(len(target), 0, -1):
                dp[i] += dp[i-1] * freq[j][ord(target[i-1]) - ord('a')]
                dp[i] %= mod
                
        return dp[len(target)]
