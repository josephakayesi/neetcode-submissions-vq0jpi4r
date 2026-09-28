class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Thought process
        - WATER = 0; LAND = 1
        - We iterate through our grid
        - At each cell we check if its land or water. 
        - If it land then we start exploring that island and accumulating the area. 
        - Once we are done accumulating the area; we update our max area for that island. 
        - We explore using dfs
        - We keep a visited set so we don't explore the same place twice. 
        - At each cell we need to accumulate the area up until we have exhausted our island; then we return the area up the dfs stack
        """

        R, C = len(grid), len(grid[0])
        WATER, LAND = 0, 1
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = set()
        res = 0 

        def out_of_bounds(nr, nc):
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == LAND:
                return False
            return True

        def dfs(r, c):
            if (r, c) in visited:
                return 0 

            visited.add((r, c))
            area = 1 

            for (dr, dc) in directions:
                nr, nc = r + dr, c + dc

                if (nr, nc) not in visited and not out_of_bounds(nr, nc):
                    area += dfs(nr, nc)
            
            return area
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == LAND and (r, c) not in visited:
                    area = dfs(r, c)
                    res = max(res, area)
        
        return res
