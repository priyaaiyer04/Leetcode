class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        l=[]
        c=0
        d=0
        for i in range(len(matrix[0])):
            c=0
            l1=[]
            while c<len(matrix):
                
                l1.append(matrix[c][i])
            
                c+=1
            l.append(l1)
        return (l)
        