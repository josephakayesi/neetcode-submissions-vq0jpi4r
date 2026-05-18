class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Thought process:
        - Keep a set of the nums. 
        - Check the length of the nums and the set
        - If the lengths are equal; no duplicates exists otherwise duplicates exists
        """

        return len(nums) != len(set(nums))