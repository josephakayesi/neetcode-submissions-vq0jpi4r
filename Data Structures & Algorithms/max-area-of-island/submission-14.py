class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 

        R, C = len(grid), len(grid[0])
        seen = set()
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def out_of_bounds(r, c):
            if 0 <= r < R and 0 <= c < C:
                return False 

            return True 

        def dfs(r, c, area):
            nonlocal max_area 
            area =  1

            seen.add((r, c))
            max_area = max(max_area, area)

            for dir_r, dir_c in directions:
                new_r, new_c = r + dir_r, c + dir_c

                # check out of bounds
                if (out_of_bounds(new_r, new_c) 
                    or (new_r, new_c) in seen 
                    or grid[new_r][new_c] == 0):

                    continue
                
                area += dfs(new_r, new_c, area)
            return area

        # Iterate through the grid
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = dfs(r, c, 0)
                    max_area = max(max_area, area)

        return max_area




        