class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        import math
        c=0
        l2=[]
        for i in nums:
            l2.append(str(i))
        l1=[]
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):
                l=[]
                l.append(i)
                l.append(j)
                l1.append(l)
        
        for i in l1:
            if math.gcd(int(l2[i[0]][0]),nums[i[1]]%10)==1:
                    c+=1
        return c 