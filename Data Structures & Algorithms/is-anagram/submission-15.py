class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
            
        freqS = Counter(s)
        freqT = Counter(t)

        for character, count in freqS.items():
            if count != freqT.get(character):
                return False

        return True
