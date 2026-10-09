# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # Map each course to its prerequisites
#         preMap = {i: [] for i in range(numCourses)}
#         for crs, pre in prerequisites:
#             preMap[crs].append(pre)

#         # Store all courses along the current DFS path
#         visiting = set()

#         def dfs(crs):
#             if crs in visiting:
#                 # Cycle detected
#                 return False
#             if preMap[crs] == []:
#                 return True

#             visiting.add(crs)
#             for pre in preMap[crs]:
#                 if not dfs(pre):
#                     return False
#             visiting.remove(crs)
#             preMap[crs] = []
#             return True

#         for c in range(numCourses):
#             if not dfs(c):
#                 return False
#         return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)   # pre -> course
            indegree[course] += 1     # course has one more prerequisite

        q = deque(n for n in range(numCourses) if indegree[n] == 0)

        taken = 0
        while q:
            node = q.popleft()
            taken += 1
            for nxt in adj[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return taken == numCourses