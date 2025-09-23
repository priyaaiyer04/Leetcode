
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        dist=[float("inf")]*n
        dist[src]=0
        for i in range(k+1):
            temp=dist[:]
            for u,v,w in flights:
                if dist[u]!=float("inf") and dist[u]+w<temp[v]:
                    temp[v]=dist[u]+w
            dist=temp
        if dist[dst]==float("inf"):
            return -1
        return dist[dst]