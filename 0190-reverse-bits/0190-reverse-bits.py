class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)  # Shift res left, then append the last bit of n
            n >>= 1                     # Shift n right to process the next bit
        return res