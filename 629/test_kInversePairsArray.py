import unittest
from kInversePairsArray import Solution


class TestSolution(unittest.TestCase):
    def test_kInversePairs(self):
        obj = Solution()

        # Test case 1
        n1, k1 = 3, 0
        self.assertEqual(obj.kInversePairs(n1, k1), 1)

        # Test case 2
        n2, k2 = 3, 1
        self.assertEqual(obj.kInversePairs(n2, k2), 2)

        # Test case 3
        n3, k3 = 3, 3
        self.assertEqual(obj.kInversePairs(n3, k3), 1)

        # Test case 4
        n4, k4 = 4, 5
        self.assertEqual(obj.kInversePairs(n4, k4), 3)

        # Test case 5
        n5, k5 = 5, 10
        self.assertEqual(obj.kInversePairs(n5, k5), 1)


if __name__ == '__main__':
    unittest.main()
