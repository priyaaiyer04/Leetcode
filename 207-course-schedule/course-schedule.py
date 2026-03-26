class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(n,visted,path):
            visited[n]=1
            path[n]=1
            for i in d[n]:
                if visited[i]==0:
                    if dfs(i,visited,path)==True:
                        return True
                elif path[i]==1:
                    return True
            path[n]=0
            return False
        d={}
        
        for i in prerequisites:
            if i[1] in d:
                if i[0] not in d[i[1]]:
                    d[i[1]].append(i[0])
            elif i[1] not in d:
                d[i[1]]=[i[0]]
            if i[0] not in d:
                d[i[0]]=[]
        visited={i:0 for i in d}
        path={i:0 for i in d}
        
        for i in d.keys():
            if visited[i]==0:
                if dfs(i,visited,path)==True: #cycle is there
                    return False 
        return True