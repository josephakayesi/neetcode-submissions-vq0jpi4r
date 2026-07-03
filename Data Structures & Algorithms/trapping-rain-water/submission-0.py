class Solution:
    """
    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
                                         i

    maxLeft = [0, 0, 2, 2, 3, 3, 3, 3, 3, 3]
                                          

    maxRight = [3, 3, 3, 3, 3, 3, 3, 2, 1, 0]
                
    leftMax = 3
    rightMax = 3

    res = 9
    """
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        res = 0

        leftMax = 0
        rightMax = 0

        for i in range(len(height)):
            maxLeft[i] = leftMax
            leftMax = max(leftMax, height[i])
        
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = rightMax
            rightMax = max(rightMax, height[i])
        
        for i in range(len(height)):
            water = max(0, min(maxLeft[i], maxRight[i]) - height[i])
            res += water
        
        return res