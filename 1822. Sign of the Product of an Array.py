"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

"""

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p=nums[0]
        for i in range(1,len(nums)):
            p*=nums[i]
        if p==0: return 0
        elif p>0: return 1
        else: return -1