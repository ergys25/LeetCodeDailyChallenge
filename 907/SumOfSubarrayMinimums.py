from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Define a constant MOD to store the value 10^9 + 7
        MOD = 10**9 + 7
        
        # Create an empty stack to store indices of elements in the array
        stack = []
        
        # Initialize the result variable to store the sum of minimums
        result = 0
        
        # Add 0 at the beginning and end of the array to handle edge cases
        arr = [0] + arr + [0]
        
        # Iterate through each element in the array along with its index
        for i, num in enumerate(arr):
            # While the stack is not empty and the current element is smaller than the element at the top of the stack
            while stack and arr[stack[-1]] > num:
                # Pop the index of the top element from the stack
                j = stack.pop()
                
                # Get the index of the element below the top element in the stack
                k = stack[-1]
                
                # Calculate the contribution of the popped element to the result
                # The contribution is the product of the element value, the length of the subarray, and the number of subarrays that include the popped element
                result += arr[j] * (i - j) * (j - k)
                
                # Take the result modulo MOD to avoid overflow
                result %= MOD
            
            # Push the current index to the stack
            stack.append(i)
        
        # Return the final result
        return result
