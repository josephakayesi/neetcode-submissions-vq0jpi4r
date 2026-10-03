from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Thought process
        - Iterate through the grid and store all treasure cells in a queue
        - For each of the treasures; explore all neighbors and add the distance from that cell to the treasure. 
        - As you explore neighbors, check if its a valid land then update its distance and add that cell to the queue. 
        """
        WATER, TREASURE, LAND = -1, 0, 2147483647
        R, C = len(grid), len(grid[0])
        q = deque()
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = set()

        def out_of_bounds(nr, nc):
            return not (0 <= nr < R and 0 <= nc < C and grid[nr][nc] == LAND and (nr, nc) not in visited)

        def append_cell(r, c):
            if out_of_bounds(r, c):
                return 
            
            q.append((r, c))
            visited.add((r, c)) # ??

        for r in range(R):
            for c in range(C):
                if grid[r][c] == TREASURE:
                    q.append((r, c))

        distance = 0
        while q:
            length = len(q)

            # By iterating for length of q at current layer or step; you ensure that you walk
            # from each treasure simultaneously allowing you to reach the closest neighboring cells earliest. 
            # This prevents having to wlak to the same cell and calculate the min distance.
            for _ in range(length):
                (r, c) = q.popleft()
                grid[r][c] = distance

                for (dr, dc) in directions:
                    nr, nc = r + dr, c + dc

                    append_cell(nr, nc)
                
            distance += 1

