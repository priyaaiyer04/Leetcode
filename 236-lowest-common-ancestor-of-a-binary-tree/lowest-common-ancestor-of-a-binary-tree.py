# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        d={}

        def desc(node):
            if node:
                left=desc(node.left)
                right=desc(node.right)
                l=[node]
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
                l+=left
                l+=right
                if p in l and q in l:
                    d[node]=True
                else:
                    d[node]=False
                return l
            else:
                return []
        desc(root)
        q=deque()
        q.append(root)
        ans=[]
        while q:
            curr=q.popleft()
            if d[curr]==True:
                ans.append(curr)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        if len(ans)==0: 
            return None 
        return ans[-1] 