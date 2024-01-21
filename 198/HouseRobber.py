# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        
        max_robbed_amount = [None] * (len(nums) + 1)
        N = len(nums)
        
        max_robbed_amount[N] = 0
        max_robbed_amount[N - 1] = nums[N - 1]
        
        for i in range(N - 2, -1, -1):
            max_robbed_amount[i] = max(max_robbed_amount[i + 1], max_robbed_amount[i + 2] + nums[i])
            
        return max_robbed_amount[0]
        