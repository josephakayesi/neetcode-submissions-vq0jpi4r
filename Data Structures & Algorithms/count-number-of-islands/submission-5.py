class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Intuition
        - To count the number of islands; start at the very first cell. 
        - Iterate through the grid and when you find `1` explore that cell using dfs. 
        - Keep a seen set to keep track of cells that have already been visited. 
        - After exploring a island; increment the islands count
        - Return the islands count
        """

        self.islands = 0
        R, C = len(grid), len(grid[0])
        self.seen = set()
        self.directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def out_of_bounds(r, c):
            if 0 <= r < R and 0 <= c < C:
                return False
            
            return True

        def dfs(r, c):
            self.seen.add((r, c))

            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc

                if (out_of_bounds(nr, nc)) or ((nr, nc) in self.seen) or (grid[nr][nc] == '0'):
                    continue

                dfs(nr, nc)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1' and (r, c) not in self.seen:
                    dfs(r, c)
                    self.islands += 1
            
        return self.islands