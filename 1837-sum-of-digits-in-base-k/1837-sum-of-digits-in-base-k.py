class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        digit_sum = 0
        
        while n > 0:
            digit_sum += n % k
            n //= k
            
        return digit_sum