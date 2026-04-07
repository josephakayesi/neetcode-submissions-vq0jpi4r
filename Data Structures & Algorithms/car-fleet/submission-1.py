class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        1 + 3 * time = destination
        position + (speed * time) = destination
        (target - position / speed) = time

        My thought process:
        Find the time it will take for each car to reach the target. 
        Store the time for each car corresponding to its position/speed index in a time list
        check which cars will take same time to reach target.
        Cars with the same time form a fleet. cars without same time for a fleet of their own.

        """

        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []
       
        # Since we are reverse sorting it; the car with the farthest position comes to the start
        # Since its one lane then the fathest car will always be at the front of the lane
        for p, s in sorted(pairs)[::-1]:
            t = (target - p) / s
            stack.append(t)
        
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

