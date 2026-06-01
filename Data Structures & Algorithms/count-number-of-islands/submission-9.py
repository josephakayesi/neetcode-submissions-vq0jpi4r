class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        LAND = '1'
        WATER = '0'

        Intuition
        - Iterate through the graph
        - At land -> explore:
            - Explore until no more land cells exists, i.e surrounded by water (dfs)
            - Count the island as an island
            - Keep track of cells that we have visited
            - Return
        - Continue until all islands are explored.
        """
        R, C = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = set()
        res = 0

        def out_of_bounds(nr, nc):
            if 0 <= nr < R and 0 <= nc < C:
                return False 
            return True 

        def dfs(r, c):
            if (r, c) in seen:
                return 
            
            seen.add((r, c))
            
            for (dr, dc) in directions:
                nr, nc = dr + r, dc + c

                if not out_of_bounds(nr, nc) and grid[nr][nc] == '1':
                    dfs(nr, nc)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1' and (r, c) not in seen:
                    dfs(r, c)
                    res += 1

        return res
