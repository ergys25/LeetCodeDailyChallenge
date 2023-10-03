# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Steps

# 1. iterate through nums2
# 2. for each element in nums2, append it to nums1
# 3. sort nums1
# 4. return nums1

# time: O(nlog(n))
# space: O(1)
# runtime: 36 ms, faster than 63.34% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 14.4 MB, less than 21.02% of Python3 online submissions for Merge Sorted Array.





class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
       
        """
        for i in range (n):
            nums1[m+i] = nums2[i]
        nums1.sort()