class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Intuition
        - Keep two sets; pacific and atlantic set. Each set contains cells that oceans can flow to
        - Add all borders to corresponding sets
        - For each cell; check with neighbors; if neighbors >= cell; then include in set
        - Find intersection between pacific set and atlantic set. 
        - Intersection gives us the cells that can both be reached from the pacific and atlantic. 
        - Return those cells
        """

        R, C = len(heights), len(heights[0])
        pacific, atlantic = set(), set() 
        res = []

        def out_of_bounds(nr, nc):
            if 0 <= nr < R and 0 <= nc < C:
                return False
            return True 

        def dfs(r, c, ocean, prev_height):
            if not out_of_bounds(r, c) and (r, c) not in ocean:
                    if heights[r][c] >= prev_height:
                        ocean.add((r, c))   
                    
                        dfs(r + 1, c, ocean, heights[r][c])
                        dfs(r, c + 1, ocean, heights[r][c])
                        dfs(r - 1, c, ocean, heights[r][c])
                        dfs(r, c - 1, ocean, heights[r][c])
                                 
        # Add column borders
        for r in range(R):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, C - 1, atlantic, heights[r][C - 1])

        # Add row borders
        for c in range(C):
            dfs(0, c, pacific, heights[0][c])
            dfs(R - 1, c, atlantic, heights[R - 1][c])

        intersection = pacific.intersection(atlantic)
        
        for r in range(R):
            for c in range(C):
                if (r, c) in intersection:
                    res.append([r, c])

        return res

        


