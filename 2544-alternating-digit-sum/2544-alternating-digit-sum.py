class Solution(object):
    def alternateDigitSum(self, n):
        total = 0
        sign = 1
        
        for ch in str(n):
            total += sign * int(ch)
            sign = -sign
            
        return total