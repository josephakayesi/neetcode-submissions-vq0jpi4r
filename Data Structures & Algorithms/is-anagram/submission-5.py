class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Intuition
        - Create an array of 26 characters. each starts with 0 in the element
        - For ecah of the strings; get the ord value and update the index corresponding to the character. 
        - At he end; check the number of occurrences of each character. if any character frequency is odd then we know it is not an anagram
        """

        s_freq = [0] * 26
        t_freq = [0] * 26

        for char in s:
            index = ord(char) - 97 
            s_freq[index] += 1 

        for char in t:
            index = ord(char) - 97
            t_freq[index] += 1 

        for i in range(len(s_freq)):
            if s_freq[i] != t_freq[i]:
                return False

        return True

        