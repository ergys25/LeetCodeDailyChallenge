# For an integer array nums, an inverse pair is a pair of integers [i, j]
# where 0 <= i < j < nums.length and nums[i] > nums[j].

# Given two integers n and k, return the number of different arrays consist of
# numbers from 1 to n such that there are exactly k inverse pairs. Since the
# answer can be huge, return it modulo 109 + 7.

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * 1001 for _ in range(1001)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                for x in range(0, min(j, i - 1) + 1):
                    if j - x >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % 1000000007

        return dp[n][k]
