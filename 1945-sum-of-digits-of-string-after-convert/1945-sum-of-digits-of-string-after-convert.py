class Solution(object):
    def getLucky(self, s, k):
        # Step 1: Convert characters to their 1-indexed alphabet position strings
        num_str = "".join(str(ord(ch) - ord('a') + 1) for ch in s)
        
        # Step 2: Transform by summing the digits k times
        total = sum(int(digit) for digit in num_str)
        
        for _ in range(k - 1):
            next_total = 0
            while total > 0:
                next_total += total % 10
                total //= 10
            total = next_total
            
        return total