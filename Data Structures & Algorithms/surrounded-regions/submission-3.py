class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        O, X, T = 'O', 'X', 'T'
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = set() 

        def out_of_bounds(nr, nc):
            return not (0 <= nr < R and 0 <= nc < C and board[nr][nc] == O)

        def dfs(r, c):
            if (r, c) in visited:
                return 

            board[r][c] = T
            visited.add((r, c))

            for (dr, dc) in directions:
                nr, nc = r + dr, c + dc

                if not out_of_bounds(nr, nc):
                    dfs(nr, nc)

        for c in range(C):
            if board[0][c] == O:
                dfs(0, c)
            
            if board[R - 1][c] == O:
                dfs(R - 1, c)
        
        for r in range(R):
            if board[r][0] == O:
                dfs(r, 0)
            
            if board[r][C - 1] == O:
                dfs(r, C - 1)

        for r in range(R):
            for c in range(C):
                if board[r][c] == O:
                    board[r][c] = X

                if board[r][c] == T:
                    board[r][c] = O
                

        
            