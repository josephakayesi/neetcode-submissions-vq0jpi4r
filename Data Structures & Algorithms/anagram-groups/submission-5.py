class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Intuition:
        - Iterate array of strs
        - array of size 26 as key for each str
        - Convert that array into key

        res = {
        "key": ["act", "cat]
        ...
            }

        Time:
        Space:
        """

        res = {}
        groups = []

        for val in strs:
            # key
            key_arr = [0] * 26
            for char in val:
                key_arr[ord(char) - 97] += 1
            
            key = '#'.join(str(num) for num in key_arr)

            if key in res:
                res[key].append(val)
            else:
                res[key] = []
                res[key].append(val)

        for item in res.values():
            groups.append(item)

        return groups
        
