class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        l=[]
        l1=[]
        s1=""
        for i in s:
            l.append(i)
        for i in goal:
            l1.append(i)
        for i in range(len(l)):
            x=l[0]
            l.pop(0)
            l.append(x)
            print(l1)
            if l==l1:
                return True
                break
