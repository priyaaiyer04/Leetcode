class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        l=0
        r=0
        s1=""
        while l<=r<len(s):
            if s[r] in s1:
                
                ans=max(ans,len(s1))
                x=l
                list1=list(s[l:r])
                list1=list1[::-1]
                idx=list1.index(s[r])
                idx=len(list1)-idx+l-1
                
                l=idx+1
                print(idx)
                s1=s[l:r+1]
                r+=1
                
            elif s[r] not in s1:
                s1+=s[r]
                r+=1
            print(l,r,s1)
        ans=max(ans,len(s1))
        return ans