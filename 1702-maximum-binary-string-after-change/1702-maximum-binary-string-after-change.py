class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # If there are fewer than 2 zeros, no changes are possible
        if binary.count('0') < 2:
            return binary
        
        # Leading ones stay untouched
        first_zero = binary.find('0')
        
        # Count zeros in the string
        zeros = binary.count('0')
        n = len(binary)
        
        # The resulting string will have exactly one '0' at index: first_zero + zeros - 1
        # All other positions will be '1'
        zero_index = first_zero + zeros - 1
        
        res = ['1'] * n
        res[zero_index] = '0'
        
        return "".join(res)