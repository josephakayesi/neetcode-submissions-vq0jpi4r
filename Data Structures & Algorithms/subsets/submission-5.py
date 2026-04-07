class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Intuition
        - To find all the possible subsets; we need to first start at the top of the decision tree. 
        - At each decision; we need to either add the elemnt or omit the element.
        - Down the tree at each decision; the element may or may not be included hence forming the possible subsets. 
        - In order to avoid duplicate subsets; we need to only include elements from the current decision onwards and not repeat elements from previous 
          iterations


          [1, 2, 3]

          res = [[], ]

          dfs(0, []):

        """

        res = []

        def dfs(index, path):
            # Base case - we have reached the max subset that can be formed. i.e index == len(nums)
            if index >= len(nums):
                res.append(path.copy())
                return

            # Include the current element 
            path.append(nums[index])
            dfs(index + 1, path)

            # Omit the current element
            path.pop()
            dfs(index + 1, path)

        dfs(0, [])

        return res
        