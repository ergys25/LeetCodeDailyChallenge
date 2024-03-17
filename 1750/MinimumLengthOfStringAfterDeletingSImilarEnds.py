# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

# Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
# Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
# The prefix and the suffix should not intersect at any index.
# The characters from the prefix and suffix must be the same.
# Delete both the prefix and the suffix.
# Return the minimum length of s after performing the above operation any number of times (possibly zero times).


class Solution:
    def minimumLength(self, s: str) -> int:
        # Initialize left and right pointers
        left, right = 0, len(s) - 1

        # Continue the loop until left and right pointers meet or the characters at left and right are not equal
        while left < right and s[left] == s[right]:
            char = s[left]  # Store the character at left pointer

            # Move the left pointer to the right until it reaches a different character
            while left <= right and s[left] == char:
                left += 1

            # Move the right pointer to the left until it reaches a different character
            while left <= right and s[right] == char:
                right -= 1

        # Return the length of the remaining string after performing the operations
        return right - left + 1


# Time: O(N)
# Space: O(1)
