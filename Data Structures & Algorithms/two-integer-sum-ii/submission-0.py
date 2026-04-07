class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        - Start two pointers at either ends of the numbers list
        - Check if val at l + r == target.
        - If lesser than target:
        -   - l += 1
        else:
            - r -= 1


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

        return [None, None]

            
        