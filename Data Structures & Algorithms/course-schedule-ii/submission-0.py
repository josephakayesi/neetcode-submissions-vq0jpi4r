class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Thought process
        - This uses a variation of the peel off method. 
        - We go through all the nodes without prerequisite; process these by walking to all neighbors and reducing the indegrees of the neighbour courses.
        - Once all prerequisisites fo rthe neighbour courses have been taken (i.e the indegree reaches 0) then we add to the queue to process that courses since it no longer has any prerequisite. 
        - The we continue until we reached the end.
        - At any time that we popleft from the queue we add that to the results
        - Once all courses have been processed we check if the number of courses taken equal the number of courses avaialble. 
        - If exists then return the result otherwise return an empty array
        """

        indegree = [0] * numCourses
        adjacency_list = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indegree[course] += 1
            adjacency_list[pre].append(course) # pre -> course

        q = deque() 

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        res = []
        while q:
            pre = q.popleft()
            res.append(pre)

            for crs in adjacency_list[pre]:
                indegree[crs] -= 1

                if indegree[crs] == 0:
                    q.append(crs)

        return res if len(res) == numCourses else []