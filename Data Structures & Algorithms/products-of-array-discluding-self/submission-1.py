class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Thought process
        - We will need to keep track of prefix and a postfix of products of nums array
        - Once we have a prefix and postfix; a simple formula to find the product of array except self 
            at each index is prefix[i - 1] * postfix[i + 1]
        - For elements at the first and last index we multiply by 1 since the index runs out of bounds.

        prefix = [1, 2, 8, 48]
        postfix = [48, 48, 24, 6]
        """

        n = len(nums)
        res = [0] * n
        prefix = [0] * n 
        postfix = [0] * n

        for i in range(n):
            if i == 0:
                prefix[i] = 1 * nums[i]
                continue
            prefix[i] = prefix[i - 1] * nums[i]

        for j in range(n - 1, -1, -1):
            if j == n - 1:
                postfix[j] = nums[j] * 1
                continue
            postfix[j] = postfix[j + 1] * nums[j]
        
        for i in range(n):
            if i == 0:
                res[i] = 1 * postfix[i + 1]
                continue
            if i == n - 1:
                res[i] = prefix[i - 1] * 1
                continue
            
            res[i] = prefix[i - 1] * postfix[i + 1]
        
        return res