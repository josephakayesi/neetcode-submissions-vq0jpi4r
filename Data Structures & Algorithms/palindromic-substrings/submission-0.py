class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        - abcabcdabc
        - Traverse string 
        - A set to keep track of palindromic strings 
        - Keep two pointers as sliding windows. 
        - For each each if its a palindrome
        - If its a palindrome update longest
        - If not; then move pointer to the next char and do palindrome check
        - 
        """

        res = 0

        for i in range(len(s)):
            l, r = i, i
            # odd length palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1


            # even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1 
        
        return res





        