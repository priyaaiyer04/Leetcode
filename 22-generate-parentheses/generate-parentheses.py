class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        def create(s,oc,cc):
            if len(s)==2*n:
                l.append("".join(s))
                return 
            if cc<oc:
                s.append(")")
                create(s,oc,cc+1)
                s.pop()
            if oc<n:
                s.append("(")
                create(s,oc+1,cc)
                s.pop()
           
        create(["("],1,0)
        return l
