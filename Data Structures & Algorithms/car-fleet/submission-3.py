class Solution:
    """
    pairs = [[4, 2], [1, 3]]
    target = 10 
    stack = [3, ] 
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        print("pairs", pairs)
        for p, s in pairs:
            time = ((target - p) / s)
            if stack and time <= stack[-1]:
                continue 
            
            stack.append(time)
        
        return len(stack)
