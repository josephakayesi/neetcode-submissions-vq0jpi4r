class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix = [1, 1, 1, 1]
        postfix = [1, 1, 1, 1]
        res 
        """
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        res = [1] * n

        for i in range(n):
            if i == 0:
                prefix[i] = 1 * nums[i]
                continue
            prefix[i] = prefix[i - 1] * nums[i]
        
        for j in range(n - 1, -1, -1):
            if j == n - 1:
                postfix[j] = nums[j] * 1
                continue
            postfix[j] = nums[j] * postfix[j + 1]
        
        for i in range(n):
            if i == 0:
                res[i] = (1 * postfix[i + 1])
                continue 
            if i == n - 1:
                res[i] = (prefix[i - 1] * 1)
                continue 
            res[i] = (prefix[i - 1] * postfix[i + 1])
            
        return res