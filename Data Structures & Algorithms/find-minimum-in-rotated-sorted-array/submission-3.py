class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Intuition
        - Looking at the problem we can use a binary search
        - In a binary search we check for the mid point. 
        - At mid we check mid + 1 and mid - 1
            - If [mid+1] > [mid-1]:
                if left > right:
                    minumum in right half 
                    update min
                if left < right:
                    minimum in left half
                    update min
            
            - If [mid+1] < [mid-1]:
                if left > right:
                    minimum in right half
                    update min
                if left < right:
                    minimum in right half 
                    update min
        
        keep going while left < right


        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]