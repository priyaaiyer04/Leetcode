class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        l=[]
        l1=[]
        l3=[]
        l5=[]
        l2=[]
        for i in words:
            if l1.count(i)==0:
                l1.append(i)
                l.append(words.count(i))
        l.sort(reverse=True)
        i=0
        l=l[i:k]
        for i in l:
            if l5.count(i)==0:
                l5.append(i)
        print(l)
        for i in l5:
            l4=[]
            for j in words:
                if i==words.count(j):
                    if l4.count(j)==0:
                        l4.append(j)
            l4.sort()
            l3.append(l4)   
        for i in l3:
            for j in i:
                l2.append(j)
                if len(l2)==k:
                    break
        return (l2)