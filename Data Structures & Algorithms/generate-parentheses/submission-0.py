class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(path, opened, closed):
            if len(path) == n * 2:
                ans.append("".join(path))
            
            if opened < n:
                path.append('(')
                backtrack(path, opened + 1, closed)
                path.pop()
                
            if closed < opened:
                path.append(')')
                backtrack(path, opened, closed + 1)
                path.pop()
        
        ans = []
        backtrack([], 0, 0)
        return ans
                