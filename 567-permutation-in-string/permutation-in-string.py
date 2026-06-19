class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l = 0
        r = 0

        l1 = list(s1)
        while l <= r < len(s2):
            if s2[r] in s1:
                flag = -1
                x=l+len(s1)
                if x>=len(s2):
                    x=len(s2)
                while r <x:
                    if s2[r] in l1:
                        l1.remove(s2[r])
                        r += 1
                    else:
                        if  s2[r] in s1:
                            flag = 0
                        break
                
                if len(l1) == 0:
                    return True
                    break
                
                if flag == -1:
                    
                    r += 1
                    l = r
                    l1 = list(s1)
                else:
                    l1.append(s2[l])
                    l+=1
                
            elif s2[r] not in s1:
                r += 1
                l=r
            
        return False