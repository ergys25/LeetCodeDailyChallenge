# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.


# Steps Dictionary

# 1. create a dictionary to store the number of times each element appears in the array
# 2. iterate through the dictionary
# 3. for each key, get the value
# 4. if the value is greater than 1, calculate the number of good pairs using the formula n(n-1)/2
# 5. add the number of good pairs to the total
# 6. return the total

# time: O(n)
# space: O(n)
# runtime: 32 ms, faster than 76.92% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 14.2 MB, less than 40.00% of Python3 online submissions for Number of Good Pairs.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0 # O(1)
        num_dict = {} # O(1)
        
        for num in nums: # O(n)
            if num in num_dict: # O(1)
                num_dict[num] += 1 # O(1)
            else:
                num_dict[num] = 1 # O(1)
        
        for num in num_dict: # O(n)
            if num_dict[num] > 1: # O(1)
                total += (num_dict[num] * (num_dict[num] - 1)) // 2 # O(1)
        
        return total # O(1)


