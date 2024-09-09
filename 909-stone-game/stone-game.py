class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        a=0
        b=0
        a1=0
        b1=0
        for i in piles:
            a+=piles[0]
            a1+=piles[len(piles)-1]
            if a1>a:
                piles.pop(len(piles)-1)
            else:
                piles.pop(0)
            b+=piles[0]
            b1+=piles[len(piles)-1]
            if b1<b:
                piles.pop(len(piles)-1)
            else:
                piles.pop(0)
        a=max(a,a1)
        b=min(b,b1)
        if a>=b:
            return True