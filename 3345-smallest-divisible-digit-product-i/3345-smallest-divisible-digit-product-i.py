class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        x = n
        while True:
            # Calculate product of digits of x
            prod = 1
            temp = x
            while temp > 0:
                prod *= (temp % 10)
                temp //= 10
                
            # Check if digit product is divisible by t
            if prod % t == 0:
                return x
            
            x += 1