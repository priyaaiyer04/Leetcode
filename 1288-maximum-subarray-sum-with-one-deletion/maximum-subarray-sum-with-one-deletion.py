class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        

        nodelete=-float('inf')
        onedelete=0
        ans=-float('inf')
        for i in range(len(arr)):
            prevnodelete=nodelete
            nodelete=max(arr[i],arr[i]+nodelete)
            onedelete=max(prevnodelete,arr[i]+onedelete)
            ans=max(ans,max(nodelete,onedelete))
        return ans