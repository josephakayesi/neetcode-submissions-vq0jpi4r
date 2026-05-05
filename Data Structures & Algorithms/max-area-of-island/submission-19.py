class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
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
                return 0
            
            seen.add((r, c))

            area = 1
            
            for (dr, dc) in directions:
                nr, nc = dr + r, dc + c

                if not out_of_bounds(nr, nc) and grid[nr][nc] == 1:
                    area += dfs(nr, nc)
            return area

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = dfs(r, c)
                    res = max(res, area)
        return res