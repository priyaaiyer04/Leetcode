class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        s=0
        c=0
        while c<k:
            x=max(gifts)
            i=gifts.index(x)
            x=math.floor(math.sqrt(x))
            gifts[i]=x
            c+=1
        return int(sum(gifts))
