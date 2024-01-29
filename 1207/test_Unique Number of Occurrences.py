import unittest
from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        freq_arr = []

        for num in arr:  # O(n)
            freq[num] += 1

        for item in freq.keys():  # O(m)
            freq_arr.append(freq[item])

        return len(freq_arr) == len(set(freq_arr))  # O(m)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_uniqueOccurrences(self):
        # Test case 1
        arr1 = [1, 2, 2, 1, 1, 3]
        self.assertTrue(self.solution.uniqueOccurrences(arr1))

        # Test case 2
        arr2 = [1, 2, 2, 3, 3, 3]
        self.assertTrue(self.solution.uniqueOccurrences(arr2))

        # Test case 3
        arr3 = [1, 1, 2, 2, 2, 3, 3, 3, 3]
        self.assertTrue(self.solution.uniqueOccurrences(arr3))

        # Test case 4
        arr4 = []
        self.assertTrue(self.solution.uniqueOccurrences(arr4))

        # Test case 5
        arr5 = [1, 1, 1, 1, 1, 1]
        self.assertTrue(self.solution.uniqueOccurrences(arr5))


if __name__ == '__main__':
    unittest.main()