class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        memo = {}

        def is_palindrome(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i >= j:
                memo[(i, j)] = True
                return memo[(i, j)]
            if s[i] != s[j]:
                memo[(i, j)] = False
                return memo[(i, j)] 
            
            memo[(i, j)] = is_palindrome(i + 1, j - 1)
            return memo[(i, j)]

        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j):
                    count += 1
        return count
