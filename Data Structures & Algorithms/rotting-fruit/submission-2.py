from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        q = deque()
        directions = [[-1, 0], [0, 1],[1, 0], [0, -1]]
        self.fresh = 0
        time = 0

        def out_of_bounds(nr, nc):
            return not (
                0 <= nr < R and 
                0 <= nc < C and  
                grid[nr][nc] == FRESH)

        def appendCell(nr, nc):
            if out_of_bounds(nr, nc):
                return
            
            grid[nr][nc] = ROTTEN
            q.append((nr, nc))
            self.fresh -= 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
                
                if grid[r][c] == FRESH:
                    self.fresh += 1

        while q and self.fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for (dr, dc) in directions:
                    nr, nc = r + dr, c + dc
                    appendCell(nr, nc)
            time += 1

        return time if self.fresh == 0 else -1

