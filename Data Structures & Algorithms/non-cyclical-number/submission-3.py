class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            total = sum(int(char) ** 2 for char in str(n))

            if total in seen:
                return False
            
            seen.add(total)
            n = total
        return True


        