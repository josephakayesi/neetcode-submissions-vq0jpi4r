class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                largest = max(largest, height * (i - index))
                start = index

            stack.append((start, h))

        for i, h in stack:
            largest = max(largest, h * (len(heights) - i))
        return largest

            







        # """
        # _   _ 
        # _   _
        # _   _
        # _   _     _
        # _   _     _
        # _   _ _ _ _
        # _ _ _ _ _ _
        #   l
        #     r


        # Intution
        # - Use two pointer l and r
        # - l and r start and the first element
        # - at each element find; the largest area that can be formed by:
        #     - first checking the area that can be formed by the single bar, 
        #     - area that can be formed by the rectange formed by l and r (i.e only valid rectangles)
        # - There are a few conditions for calculating the largest area. 
        # - When l == r:
        #     largest = max(l*1, largest)
        #     r += 1
        # - When r < l:
        #     largest = max((index(r) - index(l)) * r), (r * 1), largest)
        #     l += 1
        # - When r > l:
        #     largest = max((index(r) - index(l)) * l, (r * 1), largest)


        # - return largest


        # heights = [7,1,7,2,2,4]
        #                l
        #                       r

        # largest = 7
        # """


        # largest = 0 

        # l, r = 0, 0

        # while r < len(heights):
        #     if l == r:
        #         largest = max(heights[l], largest)
        #         r += 1
        #         continue 

        #     if heights[r] < heights[l]:
        #         width = (r - l) + 1 
        #         largest = max(width * r, r, largest)
        #         r += 1
        #         continue 

        #     if heights[r] > heights[l]:
        #         width = (r - l) + 1 
        #         largest = max(width * l, r, largest)
        #         l += 1
        #         continue

        # return largest


