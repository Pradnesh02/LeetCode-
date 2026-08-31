import math

class Solution:
    def isThree(self, n: int) -> bool:
        # A number has exactly 3 positive divisors if and only if
        # it is the square of a prime number (divisors: 1, p, p^2).
        r = int(math.isqrt(n))
        if r * r != n:
            return False
        
        # Check if r is prime
        if r < 2:
            return False
        
        for i in range(2, int(math.isqrt(r)) + 1):
            if r % i == 0:
                return False
                
        return True