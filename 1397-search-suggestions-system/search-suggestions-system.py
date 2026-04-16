class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()

        ans=[]
        for i in range(1,len(searchWord)+1):
            l=[]
            for j in products:
                if searchWord[0:i]==j[0:i]:
                    l.append(j)
            l=l[0:3]
            ans.append(l)
        return ans