# 70. Climbing Stairs
# Solved
# Easy
# Topics
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
    

# Time: O(n)
# Space: O(n)
# Runtime: 32 ms, faster than 50.50% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14.4 MB, less than 11.11% of Python3 online submissions for Climbing Stairs.
