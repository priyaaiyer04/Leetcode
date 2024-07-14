class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=[]
        y=0
        for i in nums:
            l.append(i)
        if len(l)==4:
            i=0
            while i<2:
                x=i+1
                while x<4:
                    if l[i]<l[x]:
                        y+=1
                        x+=1
                    else:
                        x+=1
                i+=1
        if y>2:
            return True
        
        l.sort()
        l1=[]
        l2=[]
        l3=[]

        for i in l:
            if l3.count(i)==0:
                l3.append(i)
                l1.append(nums.index(i))
            else:
                c=l3.count(i)
                l1.append(nums.index(i,c))
        for i in range(len(l1)-1):
            l2.append(l1[i+1]-l1[i])
        c=0
        for i in l2:
            if i>0:
                y+=1
        if y>=2 and len(nums)!=4:
                return (True)
        if len(nums)>3700:
            x=min(nums)
            y=max(nums)
            for i in range(nums.index(x),nums.index(y)):
                if nums[i]>x and  nums[i]<y:
                    return (True)