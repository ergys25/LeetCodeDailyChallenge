import unittest
from HouseRobber import Solution

class TestHouseRobber(unittest.TestCase):
    def test_rob(self):
        obj = Solution()

        # Test case 1: Rob houses [1, 2, 3, 1] and get maximum money 4
        nums1 = [1, 2, 3, 1]
        self.assertEqual(obj.rob(nums1), 4)

        # Test case 2: Rob houses [2, 7, 9, 3, 1] and get maximum money 12
        nums2 = [2, 7, 9, 3, 1]
        self.assertEqual(obj.rob(nums2), 12)

        # Test case 3: Rob houses [2, 1, 1, 2] and get maximum money 4
        nums3 = [2, 1, 1, 2]
        self.assertEqual(obj.rob(nums3), 4)

        # Test case 4: Rob houses [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and get maximum money 30
        nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(obj.rob(nums4), 30)

        # Test case 5: Rob houses [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] and get maximum money 30
        nums5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(obj.rob(nums5), 30)

        # Test case 6: Rob houses [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] and get maximum money 5
        nums6 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(obj.rob(nums6), 5)

        # Test case 7: Rob houses [1, 3, 1, 3, 100] and get maximum money 103
        nums7 = [1, 3, 1, 3, 100]
        self.assertEqual(obj.rob(nums7), 103)

        # Test case 8: Rob no houses and get maximum money 0
        nums8 = []
        self.assertEqual(obj.rob(nums8), 0)
        
        # Test case 9: Rob no houses and get maximum money 0 (Empty list)
        nums9 = []
        self.assertEqual(obj.rob(nums9), 0)

        # Test case 10: Rob a single house [5] and get maximum money 5
        nums10 = [5]
        self.assertEqual(obj.rob(nums10), 5)

        # Test case 11: Rob two houses [3, 3] with equal money and get maximum money 3
        nums11 = [3, 3]
        self.assertEqual(obj.rob(nums11), 3)

        # Test case 12: Rob two houses [2, 4] with different money and get maximum money 4
        nums12 = [2, 4]
        self.assertEqual(obj.rob(nums12), 4)

        # Test case 13: Rob three houses [1, 2, 3] with increasing money and get maximum money 4
        nums13 = [1, 2, 3]
        self.assertEqual(obj.rob(nums13), 4)

        # Test case 14: Rob three houses [3, 2, 1] with decreasing money and get maximum money 4
        nums14 = [3, 2, 1]
        self.assertEqual(obj.rob(nums14), 4)

        # Test case 15: Rob three houses [1, 3, 2] with alternating money and get maximum money 3
        nums15 = [1, 3, 2]
        self.assertEqual(obj.rob(nums15), 3)

        # Test case 16: Rob 1000 houses with money 1 each and get maximum money 500
        nums16 = [1] * 1000
        self.assertEqual(obj.rob(nums16), 500)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
