class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Assumptions
        - All elements in the list are strings
        - All elements are valid alphabets
        - Elements can be a mix of uppercase and lowercase characters. Results should be case-insensitive
        - Return the results in any order. 

        Intuition
        - Iterate through strs list.
        - Keep another key, value pair in the form groups = {key: []}
        - For each str in the list; create a deterministic key. (i.e) anagrams should result in the same key when hashed
        - Add the str to the corresponding key in the groups hash
        - Return the groups from the hash

        eat -> "key1"
        tea -> "key1"
        tan -> "key2"

        groups = {key1: [eat, tea], key2: [tan]}

        1010
        1101

        Time: O(n * k)
        Space: O(n) 
        """

        groups = defaultdict(list)

        def key(s):
            # 26 indices corresponding to 26 english aplhabet characters
            keystring = [0] * 26

            for char in s:
                ascii = ord(char.lower()) - ord('a')
                keystring[ascii] += 1
            
            # Join using a '#' to avoid collisions
            return '#'.join(str(i) for i in keystring)

        for s in strs:
            groups[key(s)].append(s)
        
        return [group for group in groups.values()]