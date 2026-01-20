class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left=0
        right=len( numbers)-1
        ans=[]
        while left<right:
            if  numbers[left]+ numbers[right]<target:
                left+=1
            elif  numbers[left]+ numbers[right]>target:
                right-=1
            else:
                ans.append(left+1)
                ans.append(right+1)
                break
        return ans