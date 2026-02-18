class Solution(object):
    def isValid(self, s):
        l=[]
        for i in s:
            
           
            if len(l)>0 and ( (l[-1]=="(" and i==')') or (l[-1]=="[" and i==']') or (l[-1]=="{" and i=='}')):
                l.pop()
            else:
                
                l.append(i)
        if len(l)==0:
            return True
        return False
