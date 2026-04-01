# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d=0
        def height(node):
            nonlocal d
            if node:
                l=height(node.left)
                r=height(node.right)
                d=max(d,l+r)
                return 1+max(l,r)
            return 0
        height(root)
        return d
        