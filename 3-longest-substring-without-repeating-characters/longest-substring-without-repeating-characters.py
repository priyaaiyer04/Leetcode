class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        l=0
        s1=""
        c=0
        while l<len(s):
            print(s1)
            if s[l] not in s1:
                s1+=s[l]
            else:
                c=max(c,len(s1))
                idx=s1.index(s[l])
                s1=s1[idx+1:]
                s1+=s[l]
            l+=1
        c=max(c,len(s1))
        return c