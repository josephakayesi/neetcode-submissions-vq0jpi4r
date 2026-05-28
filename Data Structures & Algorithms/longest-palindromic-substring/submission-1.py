class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.longest = ""
        
        def out_of_bounds(l, r):
            return not (0 <= l and len(s) > r)
        
        def scan(l, r):
            while not out_of_bounds(l, r):
                if s[l] != s[r]:
                    return

                if r - l >= len(self.longest):
                    self.longest = s[l:r + 1]
                
                l -= 1
                r += 1
          
        for i in range(n):
            scan(i, i)
            scan(i, i + 1)
        
        return self.longest