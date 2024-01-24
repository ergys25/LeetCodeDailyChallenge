import unittest
from PseudoPalindromicPaths import Solution
from TreeNode import TreeNode


class TestPseudoPalindromicPaths(unittest.TestCase):
    def test_pseudoPalindromicPaths(self):
        obj = Solution()

        # Test case 1
        #   2
        #  / \
        # 1   3
        root1 = TreeNode(2)
        root1.left = TreeNode(1)
        root1.right = TreeNode(3)
        self.assertEqual(obj.pseudoPalindromicPaths(root1), 0)

        # Test case 2
        #   2
        #  / \
        # 1   1
        root2 = TreeNode(2)
        root2.left = TreeNode(1)
        root2.right = TreeNode(1)
        self.assertEqual(obj.pseudoPalindromicPaths(root2), 0)

        # Test case 3
        #     1
        #    / \
        #   2   3
        #  / \   \
        # 3   1   1
        root3 = TreeNode(1)
        root3.left = TreeNode(2)
        root3.right = TreeNode(3)
        root3.left.left = TreeNode(3)
        root3.left.right = TreeNode(1)
        root3.right.right = TreeNode(1)
        self.assertEqual(obj.pseudoPalindromicPaths(root3), 2)


if __name__ == '__main__':
    unittest.main()
