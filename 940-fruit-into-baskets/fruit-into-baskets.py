class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l=0
        r=0
        ans=0
        l1=[]
        while l<=r<len(fruits):
            
            if fruits[r] in l1:
                r+=1
            elif fruits[r] not in l1 and len(l1)<2:
                l1.append(fruits[r])
                r+=1
            elif fruits[r] not in l1 and len(l1)==2:
                print(l1,fruits[r],r)
                ans=max(ans,r-l)
                if r-l>=len(fruits)-(l+1):
                    break
                x=fruits[l]
                while fruits[l]==x:
                    l+=1
                l1.remove(x)
                r=l
                print(l1,fruits[r],r)
        if len(l1)<=2:
            ans=max(ans,r-l)   
        return ans