from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Create a frequency table
        freq = Counter(s)

        # Initialize an empty result string
        result = ""

        # Iterate over the order string and append characters to the result string
        for char in order:
            result += char * freq[char]
            freq[char] = 0  # Mark character as processed

        # Append any remaining characters not in the specified order
        for char, count in freq.items():
            result += char * count

        # Return the result
        return result
