class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = [0] * 26
        
        for i in range(len(s)):
            ascii_1 = ord(s[i]) - ord('a')
            ascii_2 = ord(t[i]) - ord('a')
            
            count[ascii_1] += 1
            count[ascii_2] -= 1
            
        for c in count:
            if c != 0:
                return False
        
        return True
        