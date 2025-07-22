class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates.sort()
        def subsetsum(start,path,total):
            if total>target:
                return
            if total==target:
                path.sort()
                if result.count(path)==0:
                    result.append(path[:])
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                subsetsum(i,path,total+candidates[i])
                path.pop()
        subsetsum(0,[],0)
        return result
