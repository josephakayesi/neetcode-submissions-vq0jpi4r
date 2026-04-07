class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Intuition:
        - l and r pointer
        - check for l == r whilst both l and r are valid alpha. 
        - If l is not valid alpha; move pointer + 1 similar is r is not valid alpha move pointer - 1
        - Keep doing this whilst l < r
        """

        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].lower().isalnum():
                l += 1
                continue 
            
            if not s[r].lower().isalnum():
                r -= 1
                continue 

            if not s[l].lower() == s[r].lower():
                return False 
            
            l += 1
            r -= 1

        return True
            
        