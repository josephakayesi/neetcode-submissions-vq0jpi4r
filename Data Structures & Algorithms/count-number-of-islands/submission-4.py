class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Intuition:
            - Start at the beginning cell [0,0]
            - From that cell keep iterating the grid
                - Find a 1 -> start of an island
                    - Iterate in all directions (up, right, down, left):
                        - If we are surrounded water; we exit and count that as one island
                        - If not continue iterating till you find water or out of bounds from the grid. 
                - Find a 0 -> water 
        - Return the number of islands
        """

        islands = 0 
        R, C = len(grid), len(grid[0])
        seen = set()
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def out_of_bounds(r, c):
            if 0 <= r < R and 0 <= c < C:
                return False 

            return True 

        def dfs(r, c):
            seen.add((r, c))

            for dir_r, dir_c in directions:
                new_r, new_c = r + dir_r, c + dir_c

                # check out of bounds
                if (out_of_bounds(new_r, new_c) 
                    or (new_r, new_c) in seen 
                    or grid[new_r][new_c] == '0'):

                    continue
                
                dfs(new_r, new_c)

        # Iterate through the grid
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1' and (r, c) not in seen:
                    islands += 1
                    dfs(r, c)

        return islands


"""

 0, 0
 0, 1
"""


        
        