class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        ans=[]
        for i in strs:
            if ''.join(sorted(i)) not in d:
                d[''.join(sorted(i))]=[i]
            else:
                d[''.join(sorted(i))].append(i)
        for i in d:
            ans.append(d[i])
        return ans