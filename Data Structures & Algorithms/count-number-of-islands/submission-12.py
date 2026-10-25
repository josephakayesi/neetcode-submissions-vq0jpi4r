class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Thought process
        - We need to iterate through the grid and find all islands. 
        - We start at the the first cell (0,0) and walk the entire grid. 
        - At each cell we check if it is a land. 
        - If it is a land then explore all its neighbours to find the island. 
        - Once we return back from the exploration, we increment our island count
        - As we explore the island; we keep track of visisted cells so we do revisit an explored cell
        - Explore using dfs. 


        Input: grid = [
            ["0","1","1","1","0"],
            ["0","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        Output: 1

        dfs(0, 1)
            dfs(-1, 1) -> # oob
            dfs(0, 2)
                dfs(-1, 2) -> #oob
                dfs(0, 3)
                    dfs(-1, 3) -> # oob
                    dfs(0, 4) -> # water
                    dfs(1, 3)
                        dfs(0, 3) -> 
                        dfs(0, 4):
                        dfs(2, 3):
                        dfs(0, 2)
                    dfs(0,, -2)
                dfs(1, 2)
                dfs(0, 1)
            dfs(1, 1)
            dfs(0, 0)

        visited = (
            (0, 1),
            (0, 2),
            (0, 3)
        )


        """

        LAND, WATER = '1', '0'
        R, C = len(grid), len(grid[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.visited = set() # (r, c)
        res = 0

        def out_of_bounds(nr, nc):
            return not (0 <= nr < R and 0 <= nc < C and grid[nr][nc] == LAND)

        def dfs(r, c):
            self.visited.add((r, c))

            for (dr, dc) in directions:
                nr, nc = dr + r, dc + c

                if (nr, nc) not in self.visited and not out_of_bounds(nr, nc):
                    dfs(nr, nc)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == LAND and (r, c) not in self.visited:
                    dfs(r, c)
                    res += 1
        return res

