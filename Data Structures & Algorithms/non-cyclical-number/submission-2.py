class Solution:

    """
    total = 37
    cyclic = 16

    seen = set(2, 4, 16, )
    """
    def isHappy(self, n: int) -> bool:
        cyclic = n
        seen = set()

        while cyclic != 1:
            total = 0

            for digit in str(cyclic):
                total += int(digit)**2

            if total == 1:
                return True 

            if total in seen:
                return False

            seen.add(total)
            cyclic = total
        
        return True


        