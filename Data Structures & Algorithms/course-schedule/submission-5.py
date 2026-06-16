class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        0 > 1
        numCourses = 2, prerequisites = [[1,0]]
        indegree = [0, 0]
        adj = [[1], []]
        q = []
        course = 1
        completed = 2
        """


        indegree = [0] * numCourses
        adj = defaultdict(list)
        q = deque()

        for (course, prerequisite) in prerequisites:
            indegree[course] += 1
            adj[prerequisite].append(course)
        
        for course in range(len(indegree)):
            if indegree[course] == 0:
                q.append(course)

        
        completed = 0
        while q:
            course = q.popleft()

            completed += 1

            for nei in adj[course]:
                indegree[nei] -= 1 

                if indegree[nei] == 0:
                    q.append(nei)

        return completed == numCourses
