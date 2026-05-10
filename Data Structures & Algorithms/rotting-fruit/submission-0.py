class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        R, C = len(grid), len(grid[0])
        q = deque()

        time = 0
        self.fresh = 0 
        seen = set()

        def out_of_bounds(nr, nc):
            if (0 <= nr < R and 0 <= nc < C and grid[nr][nc] == FRESH and (nr, nc) not in seen):
                return False
            return True

        def appendCell(nr, nc):
            if not out_of_bounds(nr, nc):
                q.append((nr, nc))
                seen.add((nr, nc))
                self.fresh -= 1

        # 1. Find number of fresh fruits and positions of rotten fruits
        for r in range(R):
            for c in range(C):
                if grid[r][c] == FRESH:
                    self.fresh += 1
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
                    seen.add((r, c))

        # 2. For each rotten fruit; convert neighbours to rotten fruits

        """
        fresh = 2
        time = 2

        q = [(1, 1)]
        """

        while q and self.fresh > 0:
            for _ in range(len(q)):
                (r, c) = q.popleft()

                grid[r][c] = ROTTEN

                appendCell(r + 1, c)
                appendCell(r, c + 1)
                appendCell(r - 1, c)
                appendCell(r, c - 1)
            time += 1
        
        return time if self.fresh == 0 else -1

