# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#
#
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: [3]
# Example 2:
#
# Input: nums = [1]
# Output: [1]
# Example 3:
#
# Input: nums = [1,2]
# Output: [1,2]
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
#


#steps
# 1. create a dictionary
# 2. iterate through the list
# 3. if the element is in the dictionary, increment the value by 1
# 4. else, add the element to the dictionary with a value of 1
# 5. create a list
# 6. iterate through the dictionary
# 7. if the value is greater than len(nums) // 3, append the key to the list
# 8. return the list

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = collections.defaultdict(int) # O(1)
        n = len(nums) / 3            # O(1)
        Solution = []               # O(1)


        for num in nums:           # O(n)
            freq[num] += 1        # O(1)


        for k,v in freq.items(): # O(n)
            if freq[k] > n:     # O(1)
                Solution.append(k) # O(1)

        return (Solution) # O(1)
    
# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 108 ms, faster than 99.78% of Python3 online submissions for Majority Element II.
# Memory Usage: 15.5 MB, less than 95.51% of Python3 online submissions for Majority Element II.


    




  