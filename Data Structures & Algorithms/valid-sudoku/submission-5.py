class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Thought process
        - Iterate through the grid
        - Keep track of three things:
            - Rows (and digits in them)
            - Columns (and digits in them)
            - Subboxes (and digits in them)
        - Each row, column and subbox can be a set
        - At each cell we check if digit exists in row, column or subbox before inserting into set
        - If digit already exists, then return False otherwise return true
        """

        R, C = len(board), len(board[0])

        rows = [set() for _ in range(R)]
        cols = [set() for _ in range(C)]
        sub = [set() for _ in range(R)]

        sub = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(R):
            for c in range(C):
                cell = board[r][c]

                if not cell.isdigit():
                    continue 

                if cell in rows[r]:
                    return False 
                
                if cell in cols[c]:
                    return False 
                
                if cell in sub[r//3][c//3]:
                    return False 
                
                rows[r].add(cell)
                cols[c].add(cell)
                sub[r//3][c//3].add(cell)
        
        return True