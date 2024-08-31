class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        x=0
        for i in range(1,len(citations)+1):
            if citations[i-1]>=i:
                x+=1
            
        return (x)