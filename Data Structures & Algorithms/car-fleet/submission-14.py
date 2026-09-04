class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Thought process
        - We need to put together the position adn the speed of each other ordered in a list
        - We order so we can arrange the starting position on the highway. Each position zipped with its speed. 
        - Zip (position, speed)
        - Sort the list
        - Iterate through each car and calculate the time it takes to reach the destination (i.e target)
        - Keep a stack that holds the time it takes each car to reach the target
        - Calculate the time and check top of stack:
            - If incoming is less than or equal to top; don't add to stack
            - Else if it is greater then we add to the stack.
        - Keep doing this until we have passed through every car. 
        - Return the len of the stack as the numebr of fleets.
        
        
        cars = [(7, 1), (4, 2), (1, 2), (0, 1)]
        time = (target - position) / speed
        stack = [3, 4.5, 10]


        target = 10, position = [1,4], speed = [3,2]
        target = 10, position = [4,1,0,7], speed = [2,2,1,1]

        """
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []

        for (pos, speed) in cars:
            time = (target - pos) / speed 

            if stack and time <= stack[-1]:
                continue 
            stack.append(time)
        
        return len(stack)

        