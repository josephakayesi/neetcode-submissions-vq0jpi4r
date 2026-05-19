class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Intution
        - Keep a hashSet that will store {num: index}
        - Iterate through the nums list
        - For each element find the difference. 
        - Check if the difference exist in the hashSet
        - If exist return [num, diff]
        - Otherwise insert the difference into the hashSet

                   i
        nums = [3, 4, 5, 6]
        target = 7

        seen = {3: 0}

        [0, 1]


        """

        seen = {}

        for i, num in enumerate(nums):
            diff = target - num 
            if diff in seen:
                return [seen[diff], i]
            
            seen[num] = i
        
        return []