import unittest
from DivideArrayIntoArraysWithMaxDifference import Solution


class TestDivideArrayIntoArraysWithMaxDifference(unittest.TestCase):
    def test_divideArray(self):
        obj = Solution()

        # Test case 1
        nums1 = [1, 2, 3, 4, 5, 6]
        k1 = 3
        expected1 = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(obj.divideArray(nums1, k1), expected1)

        # Test case 2
        nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k2 = 3
        expected2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(obj.divideArray(nums2, k2), expected2)

        # Test case 3
        nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k3 = 4
        expected3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Update the expected output
        self.assertEqual(obj.divideArray(nums3, k3), expected3)

        # Test case 4
        nums4 = [1, 2, 3, 4, 5, 6, 7, 8]
        k4 = 3
        expected4 = []
        self.assertEqual(obj.divideArray(nums4, k4), expected4)

        # Test case 5
        nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        k5 = 4
        expected5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(obj.divideArray(nums5, k5), expected5)

if __name__ == '__main__':
    unittest.main()
