# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        freq_arr = []

        for num in arr:  # O(n)
            freq[num] += 1

        for item in freq.keys():  # O(m)
            freq_arr.append(freq[item])

        return len(freq_arr) == len(set(freq_arr))  # O(m)

# Space Complexity: O(m)
# Time Complexity: O(n + m)
