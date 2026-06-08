class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        ans = 0
        l = 0
        r = 0
        l1 = []
        if len(fruits)==fruits.count(fruits[0]):
            return len(fruits)
        while l <= r < len(fruits):
            if fruits[r] in l1:
                l1.append(fruits[r])
                r += 1

            elif fruits[r] not in l1 and (
                len(l1) == 0 or len(l1) == l1.count(l1[0])
            ):
                l1.append(fruits[r])
                r += 1

            elif fruits[r] not in l1 and len(l1) != l1.count(l1[0]):
                
                ans = max(ans, r - l)

                l1 = l1[::-1]
                x = l1[0]
                idx=0
                while idx<len(l1) and  l1[idx]==x:
                    idx+=1
                idx = len(l1) - idx
                
                l1 = l1[::-1]
                l1 = l1[idx:]
                l += idx

            

        ans = max(ans, r - l)
        return ans