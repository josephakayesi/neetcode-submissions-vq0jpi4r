class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Intuition
        - Keep two pointers
        - Start at the 



        - [1,8,6,2,5,4,8,3,7]
           l               r

           area = (r - l + 1) * min(height[l], height[r])

        """
        max_area = 0
        l = 0
        r = len(height) - 1 

        while l < r:
            max_area = max(max_area, (r - l) * min(height[l], height[r]))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
        