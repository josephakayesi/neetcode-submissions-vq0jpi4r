class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Intuition
        - Elements are sorted in nums
        - We use two pointers; i = 0, j = n - 1
        - Iterate while i != j
        - Check if i + j == target
        - If not:
            i + j < target:
                i += 1
            else:
                j -= 1
                  i   j
        numbers = [1, 2, 3, 4]
        target = 3
        """

        i, j = 0, len(numbers) - 1

        while i != j:
            total = numbers[i] + numbers[j]

            if total == target:
                return [i + 1, j + 1]
            
            if total < target:
                i += 1
            else:
                j -= 1
        
        return []