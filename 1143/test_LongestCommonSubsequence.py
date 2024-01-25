import unittest
from LongestCommonSubsequence import Solution


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_longestCommonSubsequence(self):
        obj = Solution()

        # Test case 1
        text1_1 = "abcde"
        text1_2 = "ace"
        self.assertEqual(obj.longestCommonSubsequence(text1_1, text1_2), 3)

        # Test case 2
        text2_1 = "abc"
        text2_2 = "abc"
        self.assertEqual(obj.longestCommonSubsequence(text2_1, text2_2), 3)

        # Test case 3
        text3_1 = "abc"
        text3_2 = "def"
        self.assertEqual(obj.longestCommonSubsequence(text3_1, text3_2), 0)


if __name__ == '__main__':
    unittest.main()
