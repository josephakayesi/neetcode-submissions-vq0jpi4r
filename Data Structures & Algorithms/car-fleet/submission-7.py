class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """

        [(7,1), (4,2), (1,2), (0,1)] > start(0):
        [(8,1), (6,2), (3,2), (1,1)] > after_first_speed(0)
        [(9,1), (8,2), (5,2), (2,1)] > after_2nd_speed(0)
        [(10,1), (10,2), (7,2), (3,1)] > after_3rd_speed(0)
        [(4,1)] > after_4th_speed(0)
        - stack = []
        - [[]]



    Input: target = 10
    position = [4,1,0,7]
    speed = [2,2,1,1]

    Output: 3

    Assumptions
    - You can only catch up and drive at the same speed

    Thought process 
    - We zip(position, speed) and then sort by position - [(7,1), (4,2), (1,2), (0,1)]
    - Cars are arranged in their natural order after sorting. 
    - Then we want to iterate through the zipped cars i.e natural
    - Calcualte time it takes to reach destination (target - position) / speed
    - For each cars target_time we append to a stack. 
    - Before appending we check if time at top of stack is either <= current time. 
    - If top <= curr: then it forms a fleet.
    - Check with incoming cars if they form a fleet with previous. 
    - At every iteration check if a fleet is formed and then increment fleet count
    - Return fleet  

--- 
    times = [3, 3, 4.5, 10]
                         ^
    top = 4.5
    stack = [3, 4.5, 10]

-----
target = 10, position = [1,4], speed = [3,2]

    times = [3, 3]
    top = 
    stack = []

    ------
    [1.0, 1.0, 3.0, 7.0, 12.0]


"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = [(p, s) for (p, s) in zip(position, speed)]
        zipped.sort(reverse=True)
        print(zipped)
        stack = []

        # print(times)

        for (p, s) in zipped:
            time = (target - p) / s

            if not stack:
                stack.append(time)
                continue 
            
            top = stack[-1]
            if time <= top:
                continue
            else:
                stack.append(time)
            
        return len(stack)

