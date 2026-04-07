class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Intuition:
        - Iterate through each cell 
        - If a cell is land then find the max area that can be formed from that cell. 
        - Update a global max with the latest maximum area
        - Make sure to keep a seen set to ensure we don't visit a repeat cell. 
        - Return the maximum area
        """

        R, C = len(grid), len(grid[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        seen = set()
        current_max = 0

        def is_out_of_bounds(r, c):
            return r < 0 or r >= R or c < 0 or c >= C

        def dfs(r, c, area):
            nonlocal current_max
            seen.add((r, c))
            current_max = max(current_max, area)

            for dir_r, dir_c in directions:
                new_r, new_c = r + dir_r, c + dir_c

                if is_out_of_bounds(new_r, new_c):
                    continue 
                
                if grid[new_r][new_c] == 1 and (new_r, new_c) not in seen:
                    area += 1
                    dfs(new_r, new_c, area)
                


        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = 1
                    dfs(r, c, area)


        return current_max