class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        l=[]
        l1=[]
        for i in range(len(customers)):
            a=customers[i][0]
            w=customers[i][1]
            if i>=1:
                
                if l[len(l)-1]<customers[i][0]:
                    f=w+customers[i][0]
                else:
                    f=w+l[len(l)-1]
            else:
                f=w+a
            l.append(f)
        
        x=0
        c=0
        for i in customers:
            x+=(l[c]-i[0])
            c+=1
        
        return float(x/float(len(customers)))
        