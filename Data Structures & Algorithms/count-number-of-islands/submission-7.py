class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Intuition:
        1 - land
        0 - water

        - Iterate through the grid and go in all directions until you meet water. 
        - For every iteration if we exit exploring the island; we return
        - Make sure to mark all seen cells to avoid recomputing
        - Once we see land we explore. 
        - We keep exploring until we finally exit. 
        - Once we exit we increase the numebr of islands. 
        - The seen set ensures that we do not repeat visiting the same island twice therefore avoiding duplicates
        - Return the number of islands seen

        Input: grid = [
            ["0","1","1","1","0"],
            ["0","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]

        seen = (
        (0, 1), (0, 2), (0, 3),
        (1, 3)

        )

        res = 0

        r = 0
        c = 0
        """
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.R, self.C = len(grid), len(grid[0])
        self.seen = set()
        res = 0 

        if not grid:
            return res 
        
        def out_of_bounds(nr, nc):
            if 0 <= nr < self.R and 0 <= nc < self.C:
                return False 
            return True

        def dfs(r, c):
            if (r, c) in self.seen:
                return 

            self.seen.add((r, c))
            
            for (dr, dc) in self.directions:
                nr, nc = (dr + r), (dc + c)
                if not out_of_bounds(nr, nc) and grid[nr][nc] != '0':
                    dfs(nr, nc)

        for r in range(self.R):
            for c in range(self.C):
                if grid[r][c] == '1' and (r, c) not in self.seen:
                    # Found the first valid unvisited land of island
                    dfs(r, c)
                    res += 1
                

        return res

        
