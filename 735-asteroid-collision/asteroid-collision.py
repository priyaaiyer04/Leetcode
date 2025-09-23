class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for ast in asteroids:
            while stack and ast<0<stack[-1]:
                if stack[-1]<-ast:
                    stack.pop()
                    continue
                if stack[-1]==-ast:
                    stack.pop()
                break
            else:
                stack.append(ast)
        return (stack)