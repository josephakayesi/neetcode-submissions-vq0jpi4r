class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        WATER = -1
        TREASURE = 0
        LAND = 2147483647

        R, C = len(grid), len(grid[0])
        queue = deque() 
        seen = set()

        def out_of_bounds(nr, nc):
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == LAND and (nr, nc) not in seen:
                return False
            return True

        def appendCell(nr, nc):
            if not out_of_bounds(nr,nc):
                queue.append((nr, nc))
                seen.add((nr, nc))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == TREASURE:
                    queue.append((r, c))

        print(queue)

        distance = 0
        while queue:
            for _ in range(len(queue)):
                (r, c) = queue.popleft() 
                grid[r][c] = distance

                appendCell(r + 1, c)
                appendCell(r, c + 1)
                appendCell(r - 1, c)
                appendCell(r, c - 1)
            
            distance += 1

