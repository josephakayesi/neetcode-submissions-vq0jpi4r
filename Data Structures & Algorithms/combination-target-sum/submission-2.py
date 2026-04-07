class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Intuition
        - You start at the root of your decision tree
        - For each level we either add the element or ignore the element. 
        - If by adding the element to the combinations does not equal the target then keep adding
        - You should keep track of your current sum do you do not exceed. 

        """
        
        res = []
        total = 0

        def dfs(index, total, path):
            if index >= len(nums) or total > target:
                return

            if total == target:
                res.append(path.copy())
                return

            path.append(nums[index])
            dfs(index, total + nums[index], path)

            path.pop()
            dfs(index + 1, total, path)

        dfs(0, 0, [])

        return res