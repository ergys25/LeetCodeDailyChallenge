class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = start = subarray_sum = 0
        subarray_count = {}

        for end in range(len(nums)):
            subarray_sum += nums[end]
            if subarray_sum == k:
                ans += 1
            if subarray_sum - k in subarray_count:
                ans += subarray_count[subarray_sum - k]
            subarray_count[subarray_sum] = subarray_count.get(subarray_sum, 0) + 1

        return ans
    
# Time complexity: O(n)
# Space complexity: O(n)
