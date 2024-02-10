# You are given an integer array nums of size n and a positive integer k.

# Divide the array into one or more arrays of size 3 satisfying the following
# conditions:

# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal
# to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy
# the conditions, return an empty array. And if there are multiple answers,
# return any of them.

class Solution:
    def divideArray(self, nums, k):
        size = len(nums)
        if size % 3 != 0:
            return []

        # Counting sort
        count = [0] * (max(nums) - min(nums) + 1)
        for num in nums:
            count[num - min(nums)] += 1

        result = []
        group_index = 0
        for i in range(len(count)):
            while count[i] > 0:
                if count[i + 1] > 0 and count[i + 2] > 0:
                    result.append([i + min(nums), i + 1 + min(nums), i + 2 +
                                   min(nums)])
                    count[i] -= 1
                    count[i + 1] -= 1
                    count[i + 2] -= 1
                    group_index += 1
                else:
                    return []
        return result
