class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l=[]
        def helper(i,curr):
            if i==len(s):
                if s not in l:
                    l.append(s)
                return 
            if curr[i].isalpha():
                curr=curr[0:i]+curr[i].upper()+curr[i+1:len(curr)]
                if curr not in l:
                    l.append(curr)
                helper(i+1,curr)
                curr=curr[0:i]+curr[i].lower()+curr[i+1:len(curr)]
                if curr not in l:
                    l.append(curr)
                helper(i+1,curr)
            else:
                helper(i+1,curr)
        helper(0,s)
        return l