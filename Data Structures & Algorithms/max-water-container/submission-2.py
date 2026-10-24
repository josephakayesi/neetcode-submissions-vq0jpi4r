class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Thought process
        - Keep two pointers that start at opposite ends of the the heights array
        - At each interval; calculate the area formed from the container.
        - Check the minimum height between the left and the right height. 
        - Move the pointer with the lesser height either forwards or backwards by one. 
        - If the heights are the same; we will move the left pointer. 
        - Whilst doing this; keep a running max that keeps track of the maximum height formed from all container intervals
        - Return the max as the result
                   0 1 2 3 4 5 6 7
        heights = [1,7,2,5,4,7,3,6]
                           l r
        res = 36
        """

        l, r = 0, len(heights) - 1
        res = 0 

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res