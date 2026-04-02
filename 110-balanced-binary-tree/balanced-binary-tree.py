# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        def height(node):
            if node:
                return 1+max(height(node.left),height(node.right))
            return 0
        s=[root]
        while s:
            curr=s.pop()
            if abs(height(curr.left)-height(curr.right))>1:
                return False
            if curr.left:
                s.append(curr.left)
            if curr.right:
                s.append(curr.right)
        return True