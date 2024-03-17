import unittest
from MinimumLengthOfStringAfterDeletingSImilarEnds import Solution


import unittest


class TestSolution(unittest.TestCase):
    """
    A test class for testing the Solution class.
    """

    def setUp(self):
        self.solution = Solution()

    def test_minimumLength(self):
        # Test case where no operations are performed
        s = "abc"
        self.assertEqual(self.solution.minimumLength(s), 3)

        # Test case where one operation is performed
        s = "aabbaa"
        self.assertEqual(self.solution.minimumLength(s), 0)

        # Test case where multiple operations are performed
        s = "abbac"
        self.assertEqual(self.solution.minimumLength(s), 5)

        # Test case where all characters are the same
        s = "aaa"
        self.assertEqual(self.solution.minimumLength(s), 0)

        # Test case where string is empty
        s = ""
        self.assertEqual(self.solution.minimumLength(s), 0)

        s = "abccba"
        self.assertEqual(self.solution.minimumLength(s), 0)

        s = "a"
        self.assertEqual(self.solution.minimumLength(s), 1)

        s = "ab"
        self.assertEqual(self.solution.minimumLength(s), 2)

        s = "aa"
        self.assertEqual(self.solution.minimumLength(s), 0)

        s = "abab"
        self.assertEqual(self.solution.minimumLength(s), 4)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
