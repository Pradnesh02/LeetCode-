class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        
        for num in range(low, high + 1):
            s = str(num)
            length = len(s)
            
            # Odd length numbers are never symmetric
            if length % 2 != 0:
                continue
                
            n = length // 2
            # Sum of first n digits vs last n digits
            sum_first = sum(int(c) for c in s[:n])
            sum_last = sum(int(c) for c in s[n:])
            
            if sum_first == sum_last:
                count += 1
                
        return count