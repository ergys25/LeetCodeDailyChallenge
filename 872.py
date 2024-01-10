# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def preorder(root, lista):
            if not root.left and not root.right:
                lista.append(root.val)
            else:
                if root.left:
                    preorder(root.left, lista)
                if root.right:
                    preorder(root.right, lista)

        l = []
        preorder(root1, l)
        r = []
        preorder(root2, r)

        return l == r
