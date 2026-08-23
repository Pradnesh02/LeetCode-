class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)
        
        # Traverse until the second to last element
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
                
        # If we stop exactly at the last element (n - 1), it's a 1-bit character
        return i == n - 1