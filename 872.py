# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def preorder(root, leaf_values):
            if not root.left and not root.right:
                leaf_values.append(root.val)
            else:
                if root.left:
                    preorder(root.left, leaf_values)
                if root.right:
                    preorder(root.right, leaf_values)

        leaf_values1 = []
        preorder(root1, leaf_values1)
        leaf_values2 = []
        preorder(root2, leaf_values2)

        return leaf_values1 == leaf_values2
