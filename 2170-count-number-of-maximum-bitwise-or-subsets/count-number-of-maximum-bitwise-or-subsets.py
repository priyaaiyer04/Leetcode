count2=0
max_or=0
class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        global count2, max_or
        count2=0
        max_or=0
        def count1(i,curr_or):
            global count2,max_or
            if i==len(nums):
                if curr_or>max_or:
                    max_or=curr_or
                    count2=1
                elif curr_or==max_or:
                  
                    count2+=1  
                return   
            count1(i+1,curr_or | nums[i])
            count1(i+1,curr_or)
        count1(0,0)
        return count2