# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.


# Steps

# 1. create a variable to store the direction of the array
# 2. iterate through the array
# 3. if the current element is greater than the previous element, set the direction to increasing
# 4. if the current element is less than the previous element, set the direction to decreasing
# 5. if the direction is increasing and the current element is less than the previous element, return False
# 6. if the direction is decreasing and the current element is greater than the previous element, return False
# 7. return True

# time: O(n)
# space: O(1)
# runtime: 848 ms, faster than 5.04% of Python3 online submissions for Monotonic Array.
# Memory Usage: 29.7 MB, less than 5.04% of Python3 online submissions for Monotonic Array.

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = None # O(1)
        
        for i in range(1, len(nums)): # O(n)
            if nums[i] > nums[i-1]: # O(1)
                if direction is None: # O(1)
                    direction = 'increasing' # O(1)
                elif direction == 'decreasing': # O(1)
                    return False # O(1)
            elif nums[i] < nums[i-1]: # O(1)
                if direction is None: # O(1)
                    direction = 'decreasing' # O(1)
                elif direction == 'increasing': # O(1)
                    return False # O(1)
        
        return True # O(1)