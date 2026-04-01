# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        curr=(root,1)
        q=deque()
        q.append(curr)
        l=[]
        if root is None:
            return 0
        while q:
            curr=q.popleft()
         
            if curr[0].left is not None:
                q.append((curr[0].left,1+curr[1]))
            if curr[0].right is not None:
                q.append((curr[0].right,1+curr[1]))
            if curr[0].left==curr[0].right==None:
                l.append(curr[1])
        
        return max(l)