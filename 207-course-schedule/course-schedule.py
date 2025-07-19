class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d={}
        for i in prerequisites:
            if i[0] not in d.keys():
                d[i[0]]=[]
            d[i[0]].append(i[1])
            if i[1] not in d.keys():
                d[i[1]]=[]
        visitedpast=set()
        def detectcycle(d,src,visited):
            if src in visitedpast:
                return False
            if src in visited:
                return True
            else:
                visited.append(src)
                for i in d[src]:
                        if detectcycle(d,i,visited):
                            return True
            visitedpast.add(src)
            return False
        for i in d.keys():
            if detectcycle(d,i,[])==True:
                return False
        return True
