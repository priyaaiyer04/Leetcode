import heapq
import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        for i in points:
            heapq.heappush(heap,(math.sqrt(i[0]**2+i[1]**2),i))
        l=[]
        print(heap)
        for i in range(k):
            x=heapq.heappop(heap)
            l.append(x[1])
        return l