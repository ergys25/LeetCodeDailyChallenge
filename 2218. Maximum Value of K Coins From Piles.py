"""
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

 
"""

class Solution(object):
    def maxValueOfCoins(self, piles, k):
        """
        :type piles: List[List[int]]
        :type k: int
        :rtype: int
        """
        dp = [[0] * (k + 1) for _ in range(len(piles) + 1)]
        for i in range(1, len(piles) + 1):
            for j in range(1, k + 1):
                cur = 0
                for x in range(min(len(piles[i - 1]), j)):
                    cur += piles[i - 1][x]
                    dp[i][j] = max(dp[i][j], cur + dp[i - 1][j - x - 1])
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
        return dp[len(piles)][k]
