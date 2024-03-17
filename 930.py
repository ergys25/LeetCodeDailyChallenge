class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0  # Variable to store the total count of subarrays with the given sum
        current_sum = 0  # Variable to store the current sum of elements

        freq = {}  # Dictionary to store the frequency of each sum encountered
        for num in nums:
            current_sum += num  # Add the current number to the current sum
            if current_sum == goal:  # If the current sum is equal to the goal sum
                total_count += 1  # Increment the total count by 1

            # Check if there is a previous sum that can be subtracted from the current sum to get the goal sum
            if current_sum - goal in freq:
                total_count += freq[current_sum - goal]  # Increment the total count by the frequency of the previous sum

            freq[current_sum] = freq.get(current_sum, 0) + 1  # Update the frequency of the current sum

        return total_count  # Return the total count of subarrays with the given sum
    
    