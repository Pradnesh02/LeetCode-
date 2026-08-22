class Solution(object):
    def sumOfEncryptedInt(self, nums):
        total_sum = 0
        
        for x in nums:
            s = str(x)
            max_digit = max(s)
            encrypted = int(max_digit * len(s))
            total_sum += encrypted
            
        return total_sum