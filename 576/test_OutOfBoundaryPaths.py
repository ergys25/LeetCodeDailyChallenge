import unittest
from OutOfBoundaryPaths import Solution


class TestOutOfBoundaryPaths(unittest.TestCase):
    def test_findPaths(self):
        obj = Solution()

        # Test case 1
        m1, n1, N1, x1, y1 = 2, 2, 2, 0, 0
        self.assertEqual(obj.findPaths(m1, n1, N1, x1, y1), 6)

        # Test case 2
        m2, n2, N2, x2, y2 = 1, 3, 3, 0, 1
        self.assertEqual(obj.findPaths(m2, n2, N2, x2, y2), 12)

        # Test case 3
        m3, n3, N3, x3, y3 = 3, 3, 3, 1, 1
        self.assertEqual(obj.findPaths(m3, n3, N3, x3, y3), 20)

        # Test case 4
        m4, n4, N4, x4, y4 = 1, 1, 1, 0, 0
        self.assertEqual(obj.findPaths(m4, n4, N4, x4, y4), 4)


if __name__ == '__main__':
    unittest.main()
