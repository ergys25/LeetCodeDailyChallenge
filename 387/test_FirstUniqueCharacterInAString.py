import unittest
from collections import defaultdict
from FirstUniqueCharacterInAString import Solution


class TestFirstUniqueCharacterInAString(unittest.TestCase):
    def test_firstUniqChar(self):
        obj = Solution()

        # Test case 1
        s1 = "leetcode"
        expected1 = 0
        self.assertEqual(obj.firstUniqChar(s1), expected1)

        # Test case 2
        s2 = "loveleetcode"
        expected2 = 2
        self.assertEqual(obj.firstUniqChar(s2), expected2)

        # Test case 3
        s3 = "aabbcc"
        expected3 = -1
        self.assertEqual(obj.firstUniqChar(s3), expected3)

        # Test case 4
        s4 = ""
        expected4 = -1
        self.assertEqual(obj.firstUniqChar(s4), expected4)


if __name__ == '__main__':
    unittest.main()