class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        sub={4 :"IV", 9 :"IX", 40:"XL", 90:"XC", 400:"CD",900 :"CM"}
        def convertroman(i):
            if i in d:
                return d[i]
            if i in sub:
                return sub[i]
            else:
                d1=sorted(d.keys())
                if i>d1[-1]:
                    return d[d1[-1]]+convertroman(i-d1[-1])
                for j in range(len(d1)):
                    if i<d1[j]:
                        x=d1[j-1]
                        return d[x]+convertroman(i-x)

        s=num
        l=[]
        while s:
            x=s//10**(len(str(s))-1)
            l.append(x*10**(len(str(s))-1))
            s=s%10**(len(str(s))-1)
        print(l)
        ans=""
        for i in l:
                ans+=convertroman(i)
        return ans