# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums)
        return nums
    
    def merge_sort(self, nums): # O(nlog(n)) 
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            
            self.merge_sort(left)
            self.merge_sort(right)
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j+= 1
                k += 1
            
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

# Runtime: 332 ms, faster than 50.00% of Python3 online submissions for Sort an Array.
# Memory Usage: 21.2 MB, less than 5.00% of Python3 online submissions for Sort an Array.
# Time complexity: O(nlog(n))
# Space complexity: O(n)

#steps
# 1. create a merge sort function
# 2. if the length of the array is greater than 1, split the array into two halves
# 3. call merge sort on each half
# 4. create three variables, i, j, and k, and set them to 0
# 5. while i is less than the length of the left array and j is less than the length of the right array, compare the values at the current index of the left and right arrays
# 6. if the value at the current index of the left array is less than the value at the current index of the right array, set the value at the current index of the original array to the value at the current index of the left array, and increment i and k
# 7. otherwise, set the value at the current index of the original array to the value at the current index of the right array, and increment j and k
# 8. while i is less than the length of the left array, set the value at the current index of the original array to the value at the current index of the left array, and increment i and k
# 9. while j is less than the length of the right array, set the value at the current index of the original array to the value at the current index of the right array, and increment j and k
# 10. return the original array