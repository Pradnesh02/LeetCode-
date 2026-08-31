class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        
        res = []
        while n != 0:
            remainder = n % -2
            n = n // -2
            
            # In Python, modulo with negative divisor can be negative:
            # e.g., 1 % -2 = -1, but base -2 digits must be 0 or 1.
            if remainder < 0:
                remainder += 2
                n += 1
            
            res.append(str(remainder))
        
        return "".join(reversed(res))