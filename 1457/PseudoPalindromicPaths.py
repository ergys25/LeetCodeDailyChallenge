from typing import Optional
from TreeNode import TreeNode
# Given a binary tree where node values are digits from 1 to 9. A path in the
# binary tree is said to be pseudo-palindromic if at least one permutation of
# the node values in the path is a palindrome. Return the number of 
# pseudo-palindromic paths going from the root node to leaf nodes.


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def traverse(node, pairs):
            if not node:
                return 0
            if node.val in pairs:
                pairs.remove(node.val)
            else:
                pairs.add(node.val)
            if not node.left and not node.right:
                return 1 if len(pairs) <= 1 else 0
            left = traverse(node.left, set(pairs))
            right = traverse(node.right, set(pairs))
            return left + right
        return traverse(root, set())
