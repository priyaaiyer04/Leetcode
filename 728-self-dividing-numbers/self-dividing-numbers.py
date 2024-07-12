class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        i=left
        l=[]
        while i<=right:
            x=str(i)
            for j in x:
                if j=='0':
                    break
                if i%int(j)!=0:
                    break
            else:
                l.append(i)
            i+=1
            
        return (l)
        