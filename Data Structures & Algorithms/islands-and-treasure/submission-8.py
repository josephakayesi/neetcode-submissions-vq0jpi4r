class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        Intuition
        - Start traversal from each gate.
        - Use bfs to visit each neighbors. 
        - Keep a run distance and update when you visit a neighbor
        - Bfs -> queue 
        - At each level of neighbors; iterate and update distance
        - Add new neighbors to the queue and repeat
        """
        WALL = -1
        GATE = 0
        EMPTY = 2147483647

        R, C = len(rooms), len(rooms[0])
        q = deque() 
        seen = set()

        def out_of_bounds(nr, nc):
            return not (0 <= nr < R and 0 <= nc < C and rooms[nr][nc] == EMPTY and (nr, nc) not in seen) 

        def appendCell(nr, nc):
            if out_of_bounds(nr, nc):
                return 

            q.append((nr, nc))
            seen.add((nr, nc))
        
        # 1. Find all gates and add to queue
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == GATE:
                    q.append((r, c))
        
        distance = 0
        while q:
            length = len(q)

            for _ in range(length):
                (r, c) = q.popleft() 

                rooms[r][c] = distance

                appendCell(r + 1, c)
                appendCell(r, c + 1)
                appendCell(r - 1, c)
                appendCell(r, c - 1)

            distance += 1
        
        return