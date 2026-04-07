class Solution:
    """
    Anagram: same characters and same frequency

    Intuition
    - I'd keep an array with a size 26 (Number of alphabets)
    - To iterate through the first string and increment the index for that character. 
    - Iterate through the second string and decrement the index for that character
    - Iterate the freq array and check if any element is not zero
    - If any element != 0 return False
    - WHen done with iteration and every value is 0 then we have a valid anagram.

    Time: O(max(s, t))
    Space: O(1)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for char in s:
            freq[ord(char) - 97] += 1 
        
        for char in t:
            freq[ord(char) - 97] -= 1 

        for i in range(len(freq)):
            if freq[i] != 0:
                return False 
        
        return True