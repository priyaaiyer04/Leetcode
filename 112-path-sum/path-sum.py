# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root==None :
            return False
        curr=(root,root.val)
        q=deque()
        q.append(curr)
        while q:
            curr=q.popleft()
            if curr[1]==targetSum and curr[0].left==None and curr[0].right==None:
                return True
            if curr[0].left:
                q.append((curr[0].left,curr[0].left.val+curr[1]))
            if curr[0].right:
                q.append((curr[0].right,curr[0].right.val+curr[1]))

        return False