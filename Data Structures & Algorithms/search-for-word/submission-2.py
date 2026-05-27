from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.found = False 
        
        def out_of_bounds(nr, nc):
            if (0 <= nr < R and 0 <= nc < C):
                return False
            return True
        
        def dfs(r, c, seen, i):
            if board[r][c] != word[i]:
                return
            if i == len(word) - 1:
                self.found = True 
                return  
 
            seen.add((r, c))
            
            for (dr, dc) in directions:
                nr, nc = dr + r, dc + c
                
                if out_of_bounds(nr, nc) or (nr, nc) in seen:
                    continue
                dfs(nr, nc, seen, i + 1)
            seen.remove((r, c))
            
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    seen = set()
                    dfs(r, c, seen, 0)
        
        return self.found 