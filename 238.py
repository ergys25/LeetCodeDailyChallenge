class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp=[]  # Create an empty list to store the intermediate products
        product=1  # Initialize the product variable to 1
        
        # Step 1: Calculate the product of all elements to the left of each element
        for i in nums:
            dp.append(product)  # Store the product of all elements to the left of the current element
            product*=i  # Update the product by multiplying it with the current element
        
        product=1  # Reset the product variable to 1
        
        # Step 2: Calculate the product of all elements to the right of each element
        for i in range(len(nums)-1,-1,-1):
            dp[i]=dp[i]*product  # Multiply the product of all elements to the left with the product of all elements to the right
            product*=nums[i]  # Update the product by multiplying it with the current element
        
        return dp  # Return the final list of products
    
# Time complexity analysis:
# The time complexity for this approach is O(n), where n is the length of the input list nums. This is because we iterate through the input list twice, once to calculate the product of all elements to the left of each element, and once to calculate the product of all elements to the right of each element. Therefore, the overall time complexity is linear with respect to the size of the input list.
# Space complexity analysis:
# The space complexity for this approach is O(n), where n is the length of the input list nums. This is because we use an additional list dp to store the intermediate products, which has the same length as the input list. Therefore, the overall space complexity is linear with respect to the size of the input list.
# Overall, this approach efficiently calculates the product of all elements in the input list except for the current element, using only linear time and space complexity.
    
