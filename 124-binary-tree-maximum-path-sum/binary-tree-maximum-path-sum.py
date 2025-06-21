# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxsum=float('-inf')
        def dfs(root):
            if root is None:
                return 0
            ls=max(dfs(root.left),0)
            rs=max(dfs(root.right),0)
            cs=ls+rs+root.val
            self.maxsum=max(self.maxsum,cs)
            return max(ls,rs)+root.val
        dfs(root)
        return self.maxsum