class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for i in strs:
            x=i
            x=''.join(sorted(x))
            if x not in d.keys():
                d[x]=[]
            d[x].append(i)
        l=[d[i] for i in d.keys()]
        return l