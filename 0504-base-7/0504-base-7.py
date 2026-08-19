class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
            
        is_negative = num < 0
        n = abs(num)
        digits = []
        
        while n > 0:
            digits.append(str(n % 7))
            n //= 7
            
        res = "".join(reversed(digits))
        return "-" + res if is_negative else res