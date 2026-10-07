from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Thought process
        - For each cell we need to find all pathways that go from the cell to both the pacific and the atlantic
        - If no pathway exist then that cell is invalid
        - Use bfs
        - For each cell lets find a pathway to the neighboring oceans
        - If there is a pathway that exists to both ocean mark as valid. 
        - So lets consider going from all the edge cells inwards
        - We find all cells that can flow to the oceans (atlantic and pacific)
        - Lets check for the cells that are common for the two oceans and then return that as the result

        - From outside in heights[r][c] <= neighbor
        - Traverse all cells for pacific and atlantic and check which neighboring reach the edges then add to the respective set
        - At the end check for cells that appear in both pacific and atlantic and return those as the resilting set
        """

        def out_of_bounds(nr, nc, visited):
            return not (0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited)


        def dfs(r, c, ocean, visited):
            
            visited.add((r, c))

            for (dr, dc) in directions:
                nr, nc = r + dr, c + dc

                if not out_of_bounds(nr, nc, visited) and heights[r][c] <= heights[nr][nc]:
                    ocean.add((nr, nc))
                    dfs(nr, nc, ocean, visited)

        atlantic, pacific = set(), set()
        R, C = len(heights), len(heights[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


        for c in range(C):
            pacific.add((0, c))
            atlantic.add((R - 1, c))

        for r in range(R):
            pacific.add((r, 0))
            atlantic.add((r, C - 1))

        for (r, c) in list(pacific):
            visited = set()
            dfs(r, c, pacific, visited)

        for (r, c) in list(atlantic):
            visited = set()
            dfs(r, c, atlantic, visited)

        return list(pacific.intersection(atlantic))
