from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Thought process
        - Keep a key-value hash. key: str, val: []
        - Iterate through each string
        - Form a key for each string that evaluates to the anagrams key
        - Append the anagram based ont he the key it hashes to. 

        - To calculate key: iterate through each character of the word
        - Find the ascii value of each character. 
        - Map to character list of size 26.
        - For each index; increment the count for that character. 
        - For a string using `~` as the delimiter. 
        """

        res = defaultdict(list)

        def key(word):
            asc = [0] * 26

            for char in word:
                asc[ord(char) - ord('a')] += 1

            return '~'.join(str(x)for x in asc)
        
        for word in strs:
            res[key(word)].append(word)

        return [x for x in res.values()]
