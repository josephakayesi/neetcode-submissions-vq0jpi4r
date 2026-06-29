class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Thought process
        - You have a sorted non-decreasing array
        - Start at opposite ends of the array. (left, right pointers)
        - Add both left and right pointers. 
        - Two conditions:
            - If total < target:
                left += 1
            - Else
                right += 1

            - If total == target:
                return [left, right]
        - If no sum found; return empty list
        """

        l, r = 0, len(numbers) - 1
        
        while l < r:
            total = numbers[l] + numbers[r]

            if total == target:
                return [l + 1, r + 1]
            
            if total < target:
                l += 1
            else:
                r -= 1
        return []