class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [int(d) for d in str(num)]
        
        # Separate and sort in descending order
        evens = sorted([d for d in digits if d % 2 == 0], reverse=True)
        odds = sorted([d for d in digits if d % 2 != 0], reverse=True)
        
        even_idx = 0
        odd_idx = 0
        result = []
        
        # Reconstruct the number with the largest available digit of the same parity
        for d in digits:
            if d % 2 == 0:
                result.append(str(evens[even_idx]))
                even_idx += 1
            else:
                result.append(str(odds[odd_idx]))
                odd_idx += 1
                
        return int("".join(result))