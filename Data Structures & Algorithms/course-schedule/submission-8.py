from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjList = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adjList[pre].append(course) # pre -> course
            indegree[course] += 1

        q = deque()
        
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        taken = 0
        while q:
            course = q.popleft()
            taken += 1

            for crs in adjList[course]:
                indegree[crs] -= 1

                if indegree[crs] == 0:
                    q.append(crs)
        
        return taken == numCourses