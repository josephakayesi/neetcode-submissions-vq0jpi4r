class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Input: temperatures = [30,38,30,36,35,40,28]
        Output: [1,4,1,2,1,0,0] 

        Brute-force -> O(n**2)

        Efficient solution
        - Keep a monotnic decreasing stack
        - For each element check if current element > stackTop
        - If greater: calculate day difference
        - Keep resolving backwards in the stack for colder days 
        - Keep doing this till we have iterated through the temperatues. 


        """

        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append([i, temp])
                continue 

            while stack and stack[-1][1] < temp:
                stack_i, stack_t = stack.pop()
                res[stack_i] = i - stack_i

            stack.append([i, temp])

        return res
            





        # res = [0] * (len(temperatures)) 

        # for i, temp in enumerate(temperatures):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temp:
        #             res[i] = j - i
        #             break
        
        # return res