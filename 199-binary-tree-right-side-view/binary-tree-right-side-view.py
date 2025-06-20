# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        l=[]
        q=deque([root])
        while q:
            x=len(q)
            if q[x-1] is not None:
                l.append(q[x-1].val)
            for i in range(x):
                curr=q.popleft()
                if curr and curr.left:
                    q.append(curr.left)
                    
                if curr and curr.right:
                    q.append(curr.right)
        return l