class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        l=[]
        ans=[0]*len(temperatures)
        
        for i in range(len(temperatures)):
            
            if len(l)>0 :
                while len(l)>0 and temperatures[i]>l[-1][0]:
                    temp=[temperatures[i],i]
                    ans[l[-1][1]]=temp[1]-l[-1][1]
                    
                    l.pop()
            l.append([temperatures[i],i])

        print(ans)
        return ans