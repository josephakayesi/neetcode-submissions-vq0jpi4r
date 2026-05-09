class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Intuition
        - For this problem we walk from the treasure chest towards the empty cells
        - Whilst walking we keep track of the distance from the treasure chest to the nearest cells. That gives the min distance
        - Keep doing this until all valid cells are visited
        - To achieve this we use a queue. 
        - First traverse the grid for all treasure chest. 
        - At each iteration; go in all directions; keeping a running distance. 
        - After completing the next move for all valid cells;
        - Repeat for the next level of cells from the the previous visited cells.
        - Only update a cell with it is land that has not yet being traversed
        """
        WATER = -1
        TREASURE = 0
        LAND = 2147483647

        R, C = len(grid), len(grid[0])
        q = deque()
        seen = set()

        def out_of_bounds(nr, nc):
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == LAND and (nr, nc) not in seen:
                return False 
            return True

        def appendCell(nr, nc):
            if out_of_bounds(nr, nc):
                return 
            q.append((nr, nc))
            seen.add((nr, nc))


        # Add all treasure cells into queue
        for r in range(R):
            for c in range(C):
                if grid[r][c] == TREASURE:
                    q.append((r, c))

        distance = 0
        while q:
            for _ in range(len(q)):
                (r, c) = q.popleft()
                
                grid[r][c] = distance
                
                appendCell(r - 1, c)
                appendCell(r, c + 1)
                appendCell(r + 1, c)
                appendCell(r, c - 1)

            distance += 1





    