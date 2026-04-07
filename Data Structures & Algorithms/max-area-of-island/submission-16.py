class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Intuition
        - Traverse the entire grid. 
        - If you reach a cell that is `1`; explore that cell
        - Whilst exploring; accumulate the total area for that island. 
        - After exploring, update the total max area seen so far
        - Do this until you have exhausted the grid. 
        """

        self.max_area = 0
        self.seen = set()
        self.directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        R, C = len(grid), len(grid[0])

        def out_of_bounds(r, c):
            if 0 <= r < R and 0 <= c < C:
                return False
            
            return True

        def dfs(r, c):
            self.seen.add((r, c))
            area = 1

            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc

                if out_of_bounds(nr, nc) or grid[nr][nc] == 0 or (nr, nc) in self.seen:
                    continue 

                area += dfs(nr, nc)
            
            return area 
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r, c) not in self.seen:
                    area = dfs(r, c)
                    self.max_area = max(self.max_area, area)

        return self.max_area