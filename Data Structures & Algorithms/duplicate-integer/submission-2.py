class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Intuition
        - Keep a hash map
        - For every element in the array; check if it exists in the hashmap, if not include it. 
        - If it exists in the hashmap however return false 
        """

        store = set()

        for num in nums:
            if num in store:
                return True 

            store.add(num)
        
        return False
        