# You are given an array of strings arr. A string s is formed by the
# concatenation of a subsequence of arr that has unique characters.
# Return the maximum possible length of s.
# A subsequence is an array that can be derived from another array by deleting
# some or no elements without changing the order of the remaining elements.


from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(current_subsequence, new_string):
            combined_string = current_subsequence + new_string
            return len(set(combined_string)) == len(
                current_subsequence) + len(new_string)

        def backtrack(index: int, current_subsequence: str, max_length: int) -> int:
            # Base case: all elements processed
            if index == len(arr):
                return max(max_length, len(current_subsequence))

            # Include the current element in the subsequence
            if is_unique(current_subsequence, arr[index]):
                max_length = backtrack(
                    index + 1,
                    current_subsequence + arr[index],
                    max_length
                )

            # Skip the current element
            max_length = backtrack(index + 1, current_subsequence, max_length)

            return max_length

        return backtrack(0, "", 0)
