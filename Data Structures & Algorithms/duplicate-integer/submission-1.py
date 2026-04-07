class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Intuition
        - Keep a hash map
        - For every element in the array; check if it exists in the hashmap, if not include it. 
        - If it exists in the hashmap however return false 
        """

        store = {}

        for num in nums:
            if store.get(num) is not None:
                return True 

            store[num] = True
        
        return False
        