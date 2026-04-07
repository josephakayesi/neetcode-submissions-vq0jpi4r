class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            key = [0] * 26 

            for char in word:
                key[ord(char) - 97] += 1

            key_str = [str(k) for k in key]
            key_str = "#".join(key_str)

            if key_str not in res:
                res[key_str] = [] 
            
            res[key_str].append(word)

        return list(res.values())
        